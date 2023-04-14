var child = document.querySelector('.child');
var parent = document.querySelector('.parent');
var x = 0;
var y = 0;
var isDragging = false;

// Push Click
child.addEventListener('mousedown', function(e) {
  x = e.offsetX;
  y = e.offsetY;
  isDragging = true;
});

//Move Mouse
parent.addEventListener('mousemove', function(e) {
  if (isDragging) {
    var parentRect = parent.getBoundingClientRect();
    var newX = e.clientX - x - parentRect.left;
    var newY = e.clientY - y - parentRect.top;

    if (newX < 0) {
      newX = 0;
    }
    if (newX > parent.clientWidth - child.offsetWidth) {
      newX = parent.clientWidth - child.offsetWidth;
    }
    if (newY < 0) {
      newY = 0;
    }
    if (newY > parent.clientHeight - child.offsetHeight) {
      newY = parent.clientHeight - child.offsetHeight;
    }

    child.style.left = newX + 'px';
    child.style.top = newY + 'px';
  }
});


//Up Click
parent.addEventListener('mouseup', function(e) {
  isDragging = false;
});

function checkCollision(element1, element2) {
  var rect1 = element1.getBoundingClientRect();
  var rect2 = element2.getBoundingClientRect();
  var x1 = rect1.left + rect1.width / 2;
  var y1 = rect1.top + rect1.height / 2;
  var x2 = rect2.left + rect2.width / 2;
  var y2 = rect2.top + rect2.height / 2;
  var distance = Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2);
  return distance < (rect1.width + rect2.width) / 2;

}