// Reference:
// https://codepen.io/m0skar/pen/WjBdVW

function addCalendarRow(tbodyRef, hour, index) {
  // Create a row using the inserRow() method and
  // specify the index where you want to add the row
  let row = tbodyRef.insertRow(-1); // We are adding at the end
  // Create table cells
  let c0 = row.insertCell(0);
  for(var cell=1; cell<= 5; cell++){
    var c = row.insertCell(cell);
    c.id = index.toString() + "_" + cell.toString();
  }
  // Add the course data
  c0.className = "headcol";
  c0.innerText = hour;
}

function fillCalendar(){
  let tableId = "calendarTable";
    // Get the table element in which you want to add row
  let tbodyRef = document.getElementById(tableId).getElementsByTagName('tbody')[0];
  for(var i=8; i<=18; i++){
    addCalendarRow(tbodyRef, i.toString() + ":00", i);
    addCalendarRow(tbodyRef, "", i+100);
  }
}

function addCourse(day, hour, label){
  var cell = document.getElementById(hour.toString() + "_" + day.toString());
  cell.innerHTML = '<div class="event double"><input id="check" type="checkbox" class="checkbox" /><label for="check"></label>' + label + '</div>';
  document.getElementById("calendarTable").focus();
  cell.focus();
}

function addCourseHandler(day, hour, label){
  return function(){
    addCourse(day, hour, label);
  }
}

function removeCourse(day, hour){
  var cell = document.getElementById(hour.toString() + "_" + day.toString());
  cell.innerHTML = "";
};

fillCalendar();
//addCourse(3,10,"Algebra II");
// removeCourse(3,10);
