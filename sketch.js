

function setup() {
  angleMode(DEGREES);
  myCanvas = createCanvas(windowWidth, windowHeight-100);
  myCanvas.parent("myCanvas");
  for(var i=0; i<5; i++){
    createEllipse(300+i*i*10, 300+i*50, diameter, diameter, "rgb(255, 0, 0)");
  }
}

function draw() {
  background("rgb(255, 255, 255)");
  display();
  if (isDragging) {
    shadow(shape);
  }
}

function mousePressed() {
  isDragging = true;
  shape = findShapeType(mouseX, mouseY);
}

function mouseReleased() {
  drag(shape, mouseX, mouseY);
}
