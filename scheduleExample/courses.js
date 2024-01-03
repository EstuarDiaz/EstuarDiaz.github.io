function addCourseRow(data) {
  let tableId = "courseTable";
  // Get the table element in which you want to add row
  let tbodyRef = document.getElementById(tableId).getElementsByTagName('tbody')[0];

  // Create a row using the inserRow() method and
  // specify the index where you want to add the row
  let row = tbodyRef.insertRow(-1); // We are adding at the end

  // Create table cells
  let c1 = row.insertCell(0);
  let c2 = row.insertCell(1);
  let c3 = row.insertCell(2);
  let c4 = row.insertCell(3);
  let c5 = row.insertCell(4);
  let c6 = row.insertCell(5);


  // Add the course data
  c1.innerText = data.code
  c2.innerText = data.name
  c3.innerText = data.professor
  c4.innerText = data.type
  c5.innerText = data.credits
  c6.innerHTML = '<a href="https://flexnow2.uni-goettingen.de/modulbeschreibungen/36907.pdf" target="_blank">See more</a>'

  var day = randomNumber(1, 5);
  var hour = randomNumber(8, 12);
  row.onclick = addCourseHandler(day, hour, data.name + " - " + data.type + "<br> (" + data.room + ')');
}

// Function to generate random number
function randomNumber(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}

// This function is executed when the HTML Body is loaded
function main(){
  coursesData.forEach((course) => {
    addCourseRow(course);
  });
}