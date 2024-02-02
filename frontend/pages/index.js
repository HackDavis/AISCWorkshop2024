import styles from '../styles/Home.module.scss';
import Image from 'next/image';

export default function Home() {
    return (
        <div className={styles.container}>
            <h1 className={styles.container_title}>HackDavis x AISC Machine Learning Projects</h1>
            <div className={styles.container_inside}>
                <div className={styles.container_button}>
                    <a href="/MLProjects">MLProjects</a>
                </div>
                <div className={styles.container_image}>
                    <Image src="/index/Home.png" alt="Home" width={500} height={600} quality={100} />
                </div>
            </div>

        </div>
    );
}
