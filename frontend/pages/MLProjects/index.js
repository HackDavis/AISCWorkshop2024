import styles from '../../styles/MLProjects.module.scss';
import Image from 'next/image';

export default function Home() {
    return (
        <div className={styles.container}>
            <h1 className={styles.container_title}>HackDavis x AISC <br />Machine Learning Projects</h1>
            <div className={styles.container_inside}>
                <div className={styles.container_button}>
                    <a href="/MLProjects/breastCancer">MLProjects</a>
                </div>
                <div className={styles.container_image}>
                    <Image src="/index/Home.png" alt="Home" width={400} height={500} quality={100} />
                </div>
            </div>

        </div>
    );
}
