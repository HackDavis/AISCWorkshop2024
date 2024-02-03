"use client";

import { useEffect, useState } from 'react';
import axios from "axios";
// Define an interface for the model data

const Models = ({props}) => {
    // const [modelData, setModelData] = useState<ModelData | null>(null);
    const [modelData, setModelData] = useState(null);

    useEffect(() => {
        const fetchModelData = async () => {
            try {
                const response = await axios.post(`http://localhost:8080/models`, { models: props});
                console.log("response data", response.data.models);
                setModelData(response.data.models);
                console.log("model data", modelData);
            } catch (error) {
                console.log("model data", modelData);
                console.error('Error fetching model data:', error);
            }
        };

        fetchModelData();
    }, [props]);

    return (
        <div>
            {modelData ? (
                <div>
                    {Object.keys(modelData).map( (key) => (
                        <div key={key}>
                            <h2>Model: {key}</h2>
                            <p>AUC Score: {modelData[key].auc_score}</p>
                            <h3>Classification Report:</h3>
                            <pre>{JSON.stringify(modelData[key].classification_report, null, 2)}</pre>
                        </div>                    
                    ))}
                </div>
            ) : (
                <p>Loading...</p>
            )}

        </div>
    );
};

export default Models;
