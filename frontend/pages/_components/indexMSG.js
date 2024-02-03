import { useEffect, useState } from "react";
import axios from "axios";

// 'message': "Hello world!",
// 'people': ["Aa", "Bb", "Cc"]


const IndexMSG = () => {
    const [msg, setMsg] = useState(null);

    console.log("HERE");
    useEffect(() => {
        const fetchMsg = async () => {
            try {
                const res = await axios.get("http://localhost:8080");
                console.log("RES", res);
                setMsg(res.data);
            } catch (error) {
                console.log(error);
            }
        }
        fetchMsg();
    }, []);

    return (
        <div>
            <h1>DUMMY MESSAGE</h1>
            {/* {msg ? <h1>{msg}</h1> : <h1>LOADING...</h1>} */}
            {msg ? (
                <div>
                    <h1>{msg.message}</h1>
                    {msg.people.map((person, index) => (
                        <h1 key={index}>{person}</h1>
                    ))}
                </div>
            ) : (
                <h1>LOADING...</h1>
            )}
        </div>
    )
}

export default IndexMSG;