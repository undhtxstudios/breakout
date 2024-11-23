'use strict';

let levelSize;
let pathLayer;
let linePathStart = vec2(0, randInt(0, 5));
let linePathEnd = vec2(38, randInt(0, 5));

let waveFreq = rand(0.06, 0.1);
let waveAmp = randInt(1, 3);

function gameInit() {
  canvasFixedSize = vec2(1280, 720);
  levelSize = vec2(38, 20);
  cameraPos = levelSize.scale(0.5);
}

function gameUpdate() {

}

function gameUpdatePost() { }

function gameRender() {
  drawLinePath(linePathStart, linePathEnd);
  drawWavePath(waveFreq, waveAmp)
}

function gameRenderPost() {
}

function setupPostProcess() {
}

engineInit(gameInit, gameUpdate, gameUpdatePost, gameRender, gameRenderPost);
