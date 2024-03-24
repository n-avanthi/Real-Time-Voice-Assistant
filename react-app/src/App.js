import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [response, setResponse] = useState('');

    const processAudio = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            const audioChunks = [];
            const audioRecorder = new MediaRecorder(stream);

            audioRecorder.addEventListener('dataavailable', event => {
                audioChunks.push(event.data);
            });

            audioRecorder.addEventListener('stop', async () => {
                const audioBlob = new Blob(audioChunks);
                const formData = new FormData();
                formData.append('audio', audioBlob);

                const response = await axios.post('http://localhost:5000', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                setResponse(response.data.text);
            });

            audioRecorder.start();
            setTimeout(() => {
                audioRecorder.stop();
            }, 5000);  // Recording for 5 seconds
        } catch (error) {
            console.error('Error processing audio:', error);
        }
    };

    return (
        <div>
            <button onClick={processAudio}>Process Audio</button>
            <p>{response}</p>
        </div>
    );
};

export default App;
