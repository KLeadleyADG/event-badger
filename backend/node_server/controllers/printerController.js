const ping = require('net-ping');
const arp = require('node-arp');
const os = require('os');
const dns = require('dns');
require('dotenv').config(); // Load environment variables from .env file

// List of known Evolis MAC address prefixes
const evolisMacPrefixes = ['00:1A:FD'];

function getNetworkPrefix() {
  const ipAddress = process.env.ROUTER_IP_ADDRESS;
  if (!ipAddress) {
    throw new Error('API_IP_ADDRESS is not defined in the .env file');
  }
  const ipParts = ipAddress.split('.');
  return `${ipParts[0]}.${ipParts[1]}.${ipParts[2]}`;
}

function getHostname(ip, callback) {
  dns.lookupService(ip, 0, (err, hostname) => {
    if (err) {
      console.error(`OS hostname resolution error for IP ${ip}: ${err}`);
      reverseLookup(ip, callback);
    } else {
      console.log(`OS hostname resolution for IP ${ip}: ${hostname}`);
      callback(hostname);
    }
  });
}

function reverseLookup(ip, callback) {
  dns.reverse(ip, (err, hostnames) => {
    if (err) {
      console.error(`DNS reverse lookup error for IP ${ip}: ${err}`);
      callback(ip); // Fallback to IP if no hostname found
    } else {
      console.log(`DNS reverse lookup for IP ${ip}: ${hostnames}`);
      callback(hostnames[0] || ip); // Use first hostname or fallback to IP
    }
  });
}

function isEvolisPrinter(macAddress) {
  console.log(`Checking if MAC address ${macAddress} is an Evolis printer`);
  return evolisMacPrefixes.some(prefix => macAddress.toUpperCase().startsWith(prefix));
}

function scanNetwork(networkPrefix, callback) {
  const session = ping.createSession();
  const printers = [];
  let pending = 0;

  console.log(`Executing network scan on prefix ${networkPrefix}`);
  for (let i = 1; i < 255; i++) {
    const ip = `${networkPrefix}.${i}`;
    pending++;
    console.log(`Pinging IP: ${ip}`);

    session.pingHost(ip, (error, target) => {
      if (!error) {
        console.log(`Ping successful for IP: ${target}`);
        arp.getMAC(target, (err, mac) => {
          if (!err && mac) {
            console.log(`MAC address for IP ${target}: ${mac}`);
            const isEvolis = isEvolisPrinter(mac);
            getHostname(target, (hostname) => {
              const name = isEvolis ? `Evolis Printer (${hostname})` : hostname;
              if (isEvolis || hostname.startsWith('EVO')) {
                printers.push({ ip: target, name, mac });
              }
              pending--;
              if (pending === 0) {
                callback(printers);
              }
            });
          } else {
            console.error(`Error getting MAC for IP ${target}: ${err}`);
            getHostname(target, (hostname) => {
              if (hostname.startsWith('EVO')) {
                printers.push({ ip: target, name: hostname, mac: 'Unknown' });
              }
              pending--;
              if (pending === 0) {
                callback(printers);
              }
            });
          }
        });
      } else {
        console.log(`Ping failed for IP: ${target}`);
        pending--;
        if (pending === 0) {
          callback(printers);
        }
      }
    });
  }
}

function getPrinters(req, res) {
  try {
    const networkPrefix = getNetworkPrefix();
    console.log(`Scanning network prefix: ${networkPrefix}`);

    scanNetwork(networkPrefix, (printers) => {
      console.log('Discovered printers:', printers);
      res.json(printers);
    });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Failed to discover printers');
  }
}

module.exports = { getPrinters };
