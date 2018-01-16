char sph[11] = {'0','0','4','2','E','1','D','E','8','8','F'};
char gal[11] = {'0','1','0','0','3','3','9','0','C','9','6'};
char lisa[11] = {'3','5','0','2','1','E','C','5','0','3','E'};
char drewser[11] = {'3','8','0','0','4','7','7','D','E','C','E'};

int dir = 8;
int pwm = 7;
const int analogInPin = A5;

char data[12];

int comparator = 2;

void setup(){
  Serial.begin(9600);
  //Serial.println("start");
  pinMode(dir, OUTPUT);
  pinMode(pwm, OUTPUT);
}
void loop(){
  if(Serial.available() > 0){
    delay(100);
    
    //clearing start byte
    Serial.read();
    
    for(int i = 0; i < 12; i++){
      data[i] = Serial.read();
    }
    Serial.println(data);
    //comparing:
    int check1 = 0;
    for(int i = 0; i < 11; i++){
      if(data[i] != sph[i]){
        check1 = 1;
      }
    }
    int check2 = 0;
    for(int i = 0; i < 11; i++){
      if(data[i] != gal[i]){
        check2 = 1;
      }
    }
    int check3 = 0;
    for(int i = 0; i < 11; i++){
      if(data[i] != lisa[i]){
        check3 = 1;
      }
    }
    int check4 = 0;
    for(int i = 0; i < 11; i++){
      if(data[i] != drewser[i]){
        check4 = 1;
      }
    }
    
    if(check1 == 0 || check2 == 0 || check3 == 0 || check4 == 0){
      //Serial.println("opening door now");
      digitalWrite(13, HIGH);
      openDoor();
    }
    //clears buffer
    while(Serial.available() > 0){
        Serial.read();
    }
  }
}

void openDoor(){
  //pull knob down
  digitalWrite(8, HIGH);
  for(int i = 0; i < 350; i++){
    digitalWrite(7, HIGH);
    delay(20);
    digitalWrite(7, LOW);
    delay(1);
  }
  
  //release knob
  digitalWrite(8, LOW);
  for(int i = 0; i < 150; i++){
    digitalWrite(7, HIGH);
    delay(20);
    digitalWrite(7, LOW);
    delay(1);
  }
  digitalWrite(8, HIGH);
  digitalWrite(7, LOW);
}


