"use strict";

let levelSize, ball, paddle, score, brickCount;


function gameInit() {
  canvasFixedSize = vec2(1280, 720);
  levelSize = vec2(38, 20);
  cameraPos = levelSize.scale(0.5);
  paddle = new Paddle(vec2(levelSize.x / 2 - 12, 1));
  score = brickCount = 0;
}

function gameUpdate() {

}

function gameUpdatePost() { }

function gameRender() {
  drawRect(cameraPos, levelSize, hsl(10, 0, 0.02));
}

function gameRenderPost() {

}

function setupPostProcess() {
}

engineInit(gameInit, gameUpdate, gameUpdatePost, gameRender, gameRenderPost);
