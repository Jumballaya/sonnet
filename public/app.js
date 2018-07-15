/* global axios document */

// Ready
function ready(fn) {
  if (
    document.attachEvent
      ? document.readyState === 'complete'
      : document.readyState !== 'loading'
  ) {
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

// Generate sonnet and append the text to the DOM
function handleGenerateClick() {
  function handleGenerate(text) {
    const output = document.getElementById('output');
    output.innerText = text;
  }

  function handleError(error) {
    const err = document.getElementById('error');
    err.innerText = error;
  }

  const url =
    'https://5j25zntnf7.execute-api.us-east-1.amazonaws.com/dev/sonnet/generate';
  axios(url)
    .then(res => {
      if (res.error) {
        handleError(res.data.error);
      } else {
        handleGenerate(res.data.sonnet);
      }
    })
    .catch(console.log);
}

ready(() => {
  handleGenerateClick();
  const btn = document.querySelector('button');
  btn.addEventListener('click', e => {
    e.preventDefault();
    handleGenerateClick();
  });
});
