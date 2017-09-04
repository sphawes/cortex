char sph[12] = {'0','0','4','2','E','1','D','E','8','8','F','5'};

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
    //Serial.print(data);
    //comparing:
    int check = 0;
    for(int i = 0; i < 12; i++){
      if(data[i] != sph[i]){
        check = 1;
      }
    }
    if(check == 0){
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
  for(int i = 0; i < 175; i++){
    digitalWrite(7, HIGH);
    delay(20);
    digitalWrite(7, LOW);
    delay(1);
  }
  digitalWrite(8, HIGH);
  digitalWrite(7, LOW);
}


