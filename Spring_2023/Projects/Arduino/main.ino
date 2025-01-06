// Samuel Bouchereau: Projet 1 - Capteurs & actionneurs

int DELrouge = 8;                             // Broche pour la DEL rouge
int DELverte = 10;                            // Broche pour la DEL verte
int BOUTON = 4;                               // Broche pour le bouton
int BUZZER = 9;                               // Broche pour le piezzo buzzer
int time = 1000;                              // Constante de temps
bool alarmeBloquee = false;                   // Variable pour indiquer si l'alarme est bloquée
bool alarmeActivee = false;                   // Variable pour indiquer si l'alarme est activée
int tentatives = 3;                           // Défini le nombre de tentatives allouées

void setup() {
  pinMode(DELrouge, OUTPUT);                  // Sortie pour la DEL rouge
  pinMode(DELverte, OUTPUT);                  // Sortie pour la DEL verte
  pinMode(BUZZER, OUTPUT);                    // Sortie pour le piezzo buzzer
  pinMode(BOUTON, INPUT);                     // Entrée pour bouton
  Serial.begin(9600);                         // Démarre la connexion série avec l'ordinateur
  Serial.println("Bienvenue: système d'alarme actif");
  digitalWrite(DELrouge, LOW);                // Éteindre la DEL rouge au démarrage
  digitalWrite(DELverte, HIGH);               // Allume la DEL verte au démarrage
}

void loop() {
  digitalWrite(DELrouge, LOW);                // Éteindre la DEL rouge
  digitalWrite(DELverte, HIGH);               // Éteindre la DEL verte
  if (digitalRead(BOUTON) == LOW) {           // Si le bouton est pressé
    if (alarmeActivee == false) {             // Si seulement l'alarme n'est pas déjà activée
      Serial.println("Intrusion détectée: Alarme déclenchée"); 
      activerAlarme();                        // Active l'alarme
    }
  }
}

void activerAlarme() {
  alarmeActivee = true;                       // Indique que l'alarme est activée
  Serial.println("Veuillez saisir le code d'identification: _ _ _ _ _"); 

  while (alarmeActivee) {                     // Boucle tant que l'alarme est activée
    digitalWrite(DELverte, LOW);              // Éteindre la DEL verte
    analogWrite(BUZZER, 200);                 // Le moteur tourne à une vitesse élevée
    digitalWrite(DELrouge, HIGH);             // Allumer la DEL rouge
    delay(time);
    analogWrite(BUZZER, 0);                   // Le moteur arrête
    digitalWrite(DELrouge, LOW);              // Éteindre la DEL rouge
    delay(time);
    
    if (Serial.available() != 0) {            // Si des données sont disponibles sur le port série
      int code = Serial.parseInt();           // Attribue à la variable 'code' la combinaison entrée par l'utilisateur
      if (code == 12345) {                    // Vérifier si le code est valide
        desactiverAlarme();                   // Désactive l'alarme
      }
      else {                                        // Si la combinaison est incorrect
        tentatives -= 1;                            // On soustrait 1 à la variable 'tentatives'
        if (tentatives <= 0){                       // Si le nombre de tentatives atteint 0
            Serial.println("Identification échouée: la centrale vous contactera sous peu");
            alarmeBloquee = true;                   // On indique que l'alarme est maintenant bloquée
            alarmeContinue();                       // Bloque l'alarme
        }
        else if (tentatives > 1) {                  // Si le nombre de tentatives est supérieur à 1
          Serial.print("Code incorrect: ");
          Serial.print(tentatives);
          Serial.println(" essais restants"); 
        }
        else if (tentatives = 1) {                  // S'il ne reste qu'une seule tentative
          Serial.print("Code incorrect: ");         // ** Deux else if sont nécessaires, essentiellement pour l'orthographe
          Serial.print(tentatives);                 // différent de "essai restant" au singulier/pluriel **
          Serial.println(" essai restant"); 
        }
      }
    }
  }
}

void desactiverAlarme() {
  alarmeActivee = false;                          // Indiquer que l'alarme est désactivée
  analogWrite(BUZZER, 0);                         // Arrêter le piezzo buzzer
  Serial.println("Alarme désactivée");
  tentatives = 3;                                 // Réinitialise le nombre de tentatives à 3
  
}

void alarmeContinue() {
  digitalWrite(DELrouge, HIGH);                   // Allume la DEL rouge
  while (alarmeBloquee = true) {                  // Boucle à l'infini tant que le programme n'est pas arrêté manuellement
    analogWrite(BUZZER, 200);                     // Le moteur tourne à une vitesse élevée
    delay(time);
    analogWrite(BUZZER, 0);                       // Le moteur arrête
    delay(time);
  }
}