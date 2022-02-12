import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
// import NavBar from '../components/NavBar';
import './Home.css';
import {useEffect, useState} from "react";
import axios from "axios";
import {API_URL} from "../utils/constants"
import NavBar from "../components/NavBar";

const Home: React.FC = () => {
  const [centers, setCenters] = useState<any>([]);

  useEffect(() => {
    axios.get(`${API_URL}/centers`).then((response) => {
      setCenters(response.data);
    });
  }, [])

  if(!centers) return null

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Tab 1</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <NavBar name={"Centers"}/>
        {/*<NavBar name="Tab 1 page" />*/}
        {centers.map((center: any) => {
          return <h1>{center.name}</h1>
        })}
      </IonContent>
    </IonPage>
  );
};

export default Home;
