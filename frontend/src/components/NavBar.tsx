import './NavBar.css';
import {IonHeader, IonTitle, IonToolbar} from "@ionic/react";

interface ContainerProps {
  name: string;
}

const NavBar: React.FC<ContainerProps> = ({ name }) => {
  return (
    <IonHeader>
      <IonToolbar>
        <IonTitle>{name}</IonTitle>
      </IonToolbar>
    </IonHeader>
  );
};

export default NavBar;
