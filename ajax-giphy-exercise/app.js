//upon submit, get value of userInput
//search through API to find the list of matching gifs for the user input 
//generate randomGif from the list
// create image to attach randomGifs url
//remove button 

const form = document.querySelector('#form');
const userInput = document.querySelector('#userInput');
const gifContainer = document.querySelector('#gifContainer');

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  const searchInput = userInput.value;
  gifData(searchInput);
  userInput.value = '';
});

async function gifData(searchInput) {
    const response = await axios.get(`https://api.giphy.com/v1/gifs/search?api_key=hyFP51uL6hfDjaI2N2sOafOAMfBNqmgy&q=${searchInput}&limit=10&offset=0&rating=g&lang=en&bundle=messaging_non_clips`);

    const gifArray = response.data.data;

    //check to see if there are gifs in the array
    //if true, generate random gif 
    if (gifArray.length > 0) {

      //generate random index from the gif array
      const randomIndex = Math.floor(Math.random() * gifArray.length);
      const randomGif = gifArray[randomIndex];
      
      //create an image and append url
      const gifImage = document.createElement('img');
      const gifUrl = randomGif.images.original.url;

      //attach randomGif image url to newly created image and append to container
      gifImage.src = gifUrl;
      gifContainer.appendChild(gifImage);
    } else {
      alert('search for more gifs !');
    }

}

//remove All gifs from gif container 
const removeBtn = document.querySelector('#removeBtn');
removeBtn.addEventListener('click', function(e) {
  gifContainer.innerHTML = '';
});
