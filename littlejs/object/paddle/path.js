'use strict';

function drawLinePath(linePathStart, linePathEnd) {
  drawLine(linePathStart, linePathEnd, 0.03, WHITE); // TODO: change color
  box2dDrawCircle(linePathEnd, 0.5, RED);
}

function drawWavePath(freq, amp) {
  let i = 0.1;
  let prevPos = vec2(0, 0), curPos = vec2(i, i);
  while (i < levelSize.x) {
    curPos = vec2(curPos.x+0.1, wave(freq, amp, i));
    drawLine(vec2(prevPos), vec2(curPos), 0.04, WHITE); // TODO: change color
    prevPos = curPos;
    i += 0.1;
  }
}