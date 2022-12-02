import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Docs.module.css";
import Link from "next/link";
import { useRouter } from "next/router";
import { useState, useEffect } from "react";
import { Spinner } from "reactstrap";
// import "bootstrap/dist/css/bootstrap.min.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash, faEdit, faPlus } from "@fortawesome/free-solid-svg-icons";

export default function Docs() {
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  useEffect(() => {
    const load = async () => {
      const res = await fetch("/api/docs/docs");
      const data = await res.json();
      setDocs(data);
      setLoading(true);
    };
    load();
  }, []);

  const [docs, setDocs] = useState([]);

  return (
    <div className={styles.container}>
      <Head>
        <title>Gestion Documental</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header className={styles.header}>
        <Link className={styles.Link} href="/">
          <h3>Gestion Documental</h3>
        </Link>
        <div className={styles.header}>
          <Link className={styles.Link} href="/docs">
            Docs
          </Link>
          <Link className={styles.Link} href="/category">
            Categories
          </Link>
          <Link className={styles.Link} href="/inventory">
            Inventory
          </Link>
        </div>
      </header>

      <main className={styles.main}>
        {loading ? (
          docs.length > 0 ? (
            <>
              <h1 className={styles.title}>Documents</h1>
              <div className={styles.grid}>
                {docs.map((doc) => (
                  <div className={styles.card} key={doc._id}>
                    <h3>{doc.Titulo}</h3>
                    <p>{doc.Autor}</p>
                    {/* <p>{doc.Editorial}</p> */}
                    <p>{doc.Genero}</p>
                    {/* <p>{doc.Edicion}</p> */}
                    <p>{doc.Icbn}</p>
                    <p>{doc.anoPublicacion}</p>
                    <Link
                      href={"/updDoc/" + doc._id}
                      className={styles.editBtn}
                    >
                      <FontAwesomeIcon
                        icon={faEdit}
                        style={{ width: "12px" }}
                      />
                    </Link>
                    <Link
                      href={"/delDoc/" + doc._id}
                      className={styles.deleteBtn}
                    >
                      <FontAwesomeIcon
                        icon={faTrash}
                        style={{ width: "12px" }}
                      />
                    </Link>
                  </div>
                ))}
              </div>
              <Link href="/addDoc" className={styles.postBtn}>
                <FontAwesomeIcon icon={faPlus} style={{ width: "25px" }} />
              </Link>
            </>
          ) : (
            <>
              <h1>No hay documentos</h1>
            </>
          )
        ) : (
          <>
            <Spinner hidden={loading} />
          </>
        )}
      </main>

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{" "}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  );
}