import express from 'express';
import http from 'http';
import { Server } from 'socket.io';
import usbDetect from 'usb-detection';
import path from 'path';
import {fileURLToPath} from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename)
const app = express();
const server = http.createServer(app);
const io = new Server(server);

usbDetect.startMonitoring();

usbDetect.on('add', (device) => {
    console.log('Device added:', device);
    io.emit('device-connected', device);
});


app.use(express.static(path.join(__dirname, '../AndroidECT/dist')));

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../AndroidECT/dist', 'index.html'));
});

server.listen(3773, () => {
    console.log('Listening on port 3773')
});