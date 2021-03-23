p5.prototype.createEllipse = function (x, y, width, height, color) {
    this.x = x;
    this.y = y;
    var ellipse_obj = {
        type: width==height ? "circle" : "ellipse",
        x: this.x,
        y: this.y,
        w: width,
        h: height,
        center: [this.x, this.y],
        col: color,
        name: P[shapes.length]
    };
    shapes.push(ellipse_obj);
}

p5.prototype.display = function () {
    // Draw lines
    fill("rgb(0,0,255)");
    var Lines = []
    angleMode(DEGREES);
    draggin_name = '.'
    if(isDragging && shape[1] !== undefined){
        draggin_name = shape[1].name;
    }
    for(var i=0; i<shapes.length; i++){
        for(var j=0; j<shapes.length; j++){
            if(i < j){
                var m = (shapes[i].y - shapes[j].y)/(shapes[i].x - shapes[j].x);
                var b = shapes[i].y - m* shapes[i].x;
                stroke(10);
                if(showLines && draggin_name != shapes[i].name && draggin_name != shapes[j].name){
                    line(0, b, windowWidth, m*windowWidth+b);
                }
                stroke(100);
                Lines.push({
                    name: shapes[i].name+shapes[j].name,
                    value: ((atan2(shapes[i].x - shapes[j].x, shapes[i].y - shapes[j].y)+180) % 180)
                });
            }
        }
    }
    Lines.sort((a, b) => (a.value > b.value) ? 1 : -1)
    var configuration = "";
    var configuration_array = "";
    for(var i=0; i<Lines.length; i++){
        configuration = configuration + Lines[i].name + " | ";
        configuration_array += "{'" + Lines[i].name[0] + "','" + Lines[i].name[1] + "'},";
    }
    fill("rgb(0,0,0)");
    text(configuration, 150, 150);
    document.getElementById("lines").value = "["+configuration_array.substring(0, configuration_array.length-1)+"]";
    // Draw points
    for(var i=0; i<shapes.length; i++){
        fill(shapes[i].col);
        ellipse(shapes[i].x, shapes[i].y, shapes[i].w, shapes[i].h);
        fill("rgb(0,0,0)");
        text(shapes[i].name, shapes[i].x-diameter, shapes[i].y-diameter);
    }
}

p5.prototype.findShapeType = function(mx, my) {
    var mini = Infinity;
    var mini_obj;
    for(var i=0; i<shapes.length; i++){
        var d = dist(shapes[i].center[0], shapes[i].center[1], mx, my);
        if(d <= mini){
            mini = d;
            mini_obj = shapes[i];
        }
    }

    if(mini_obj != undefined){
        if(mini_obj.type == "circle"){
            var radius = mini_obj.w/2;
            if(dist(mx, my, mini_obj.x, mini_obj.y) <= radius){
                return ["circle", mini_obj];
            }
            else{
                return ["background", undefined];
            }
        }
    }
    else return ["background", undefined];
}
