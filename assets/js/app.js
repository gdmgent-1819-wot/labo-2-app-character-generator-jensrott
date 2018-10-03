init = () => {
  const config = {
    apiKey: 'AIzaSyDZP2arT7tMz-m9IebrawP-89Lus7fjehU',
    authDomain: 'wot1-34143.firebaseapp.com',
    databaseURL: 'https://wot1-34143.firebaseio.com',
    projectId: 'wot1-34143',
    storageBucket: 'wot1-34143.appspot.com',
    messagingSenderId: '441395008651'
  };
  firebase.initializeApp(config);
};

createPixels = () => {
  let container = document.querySelector('.grid-container');
  for (let i = 0; i < 64; i++) {
    let pixel = document.createElement('div');
    pixel.classList.add('pixel');
    container.appendChild(pixel);
  }
};

createArcadeCharacterSelf = () => {
  let patternsArray = [];
  let allPixels = document.querySelectorAll('.pixel');
  let save_button = document.querySelector('.save-button');
  let firebaseDB = firebase.database();
  console.log(allPixels);

  allPixels.forEach(pixel => {
    pixel.addEventListener('click', e => {
      pixel.classList.add('pixel-on');
      let JsonPixel = JSON.stringify(pixel);
      patternsArray.push(JsonPixel);
      console.log(patternsArray);
      console.log(pixel);
    });
  });

  /* Save in the database */
  save_button.addEventListener('click', e => {
    firebaseDB
      .ref()
      .child('patterns')
      .set({ patternsArray });
    /* TODO */
    console.log(`Saved following pattern : ${patternsArray}`);
  });
};

/* TODO */
GenerateRandomArcadeCharacter = (columns, w, h) => {
  let tempstr = '';
};

/* Dirty for now */
resetGrid = () => {
  let allPixels = document.querySelectorAll('.pixel');

  allPixels.forEach(pixel => {
    pixel.classList.remove('pixel-on');
  });
};
let resetButton = document.querySelector('.reset-button');
resetButton.addEventListener('click', e => {
  resetGrid();
  console.log('Clear');
});

init();

createPixels();

createArcadeCharacterSelf();
