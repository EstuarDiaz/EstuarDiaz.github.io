var isDragging = false;

//Calculates the new position for the shape which is being dragged
//Gets called when mouse is released OR at end of dragging
//Needs to be called in mousePressed() function of p5
p5.prototype.drag = function (obj, mx, my) {
    isDragging = false;
    this.shape_obj = obj[1];
    this.shape_type = obj[0];
    var index = shapes.indexOf(this.shape_obj);

    if(index > -1){
        shapes.splice(index, 1);
    }
    if(this.shape_type == "circle" || this.shape_type == "ellipse"){
        var repositioned_obj = {
            type: this.shape_type,
            x: mx,
            y: my,
            w: this.shape_obj.w,
            h: this.shape_obj.h,
            center: [mx, my],
            col: this.shape_obj.col,
            name: this.shape_obj.name
        };
        shapes.push(repositioned_obj);
    }
}

//Creates a shadow of the object (currently being dragged) under the cursor
//Needs to be called in draw() after display() if isDragging is true
p5.prototype.shadow = function (obj) {
    this.shape_type = obj[0];
    this.shape_obj = obj[1];
    push();
    fill('rgba(220, 222, 226, 0.30)');
    if(this.shape_type == "circle" || this.shape_type == "ellipse"){
        ellipse(mouseX, mouseY, this.shape_obj.w, this.shape_obj.h);
    }
    pop();
}