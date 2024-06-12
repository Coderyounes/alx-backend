import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient({
  url: 'redis://127.0.0.1:6379',
});

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log(`Redis client not connected to server: ${err}`));

const setNewSchool = async (schoolName, value) => {
  const reply = await client.set(schoolName, value);
  console.log('REPLY: ', reply);
};

const displaySchoolValue = async (schoolName) => {
  const value = await client.get(schoolName);
  console.log(value);
};

(async () => {
  await client.connect().catch(console.error);
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
