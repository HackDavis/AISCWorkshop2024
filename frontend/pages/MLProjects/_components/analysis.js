
"use client";

import { useEffect, useState } from 'react';
import axios from 'axios';
import dotenv from 'dotenv';
dotenv.config();

const Analysis = () => {
    const [imageUrl, setImageUrl] = useState('');
    const local_server_endpoint = "http://localhost:8080" // TODO
    useEffect(() => {
        const fetchImage = async () => {
            try {
                const response = await axios.get(`${local_server_endpoint}/analysis`, { responseType: 'blob' });
                const imageUrl = URL.createObjectURL(response.data);
                // console.log("image url", imageUrl);
                setImageUrl(imageUrl);
            } catch (error) {
                console.error('Error fetching image:', error);
            }
        };

        fetchImage();
    }, []);

    return (
        <div style={{}}>
            {imageUrl ? (
                // <Image />
                <img src={imageUrl} alt="Generated Image" style={{ width: '100%', height: '100%' }} />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default Analysis;
