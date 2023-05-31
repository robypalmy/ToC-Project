<!-- create a toolbar in vue with an input for a file -->
<template>
  <v-content :class="{ 'dark-mode': isDarkMode, 'light-mode': !isDarkMode }" class="v-content">
    <v-container fill-height>
      <v-row style="margin: 0" justify="center">
        <v-col cols="auto">
          <v-card :class="{ 'lightBackground': isDarkMode, 'darkBackground': !isDarkMode }" width="45vw" height="30vh"
            raised>
            <v-card-title :class="{ 'white-text': isDarkMode, 'black-text': !isDarkMode }"><b>Select your
                file:</b></v-card-title>
            <br>
            <v-card-text class="inputContainer">
              <v-file-input accept=".txt" label="Click here to select a .txt file" outlined v-model="chosenFiles"
                :class="{ 'inputboxlight': isDarkMode, 'inputboxdark': !isDarkMode }" v-on:click="testFunction">
              </v-file-input>
            </v-card-text>
            <v-card-actions class="btnContainer">
              <v-btn right class="readFileBtn" @click="importTxt"><b>Read File</b></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="auto">
          <v-card :class="{ 'lightBackground': isDarkMode, 'darkBackground': !isDarkMode }" width="45vw" height="51vh"
            class="cardContainer" raised>
            <v-card-title :class="{ 'white-text': isDarkMode, 'black-text': !isDarkMode }"><b>File
                contents:</b></v-card-title>
            <v-card-text class="cardText">
              <p class="file_contents" :class="{ 'white-text': isDarkMode, 'black-text': !isDarkMode }">{{ file_contents
              }}</p>
              <!-- Display image here -->
              <img class="imgOutput" style="max-height: 300px" :src="imageSrc" :key="imageSrc" alt="Image from backend"
                v-if="imageSrc" />
            </v-card-text>
          </v-card>
        </v-col>

      </v-row>
    </v-container>
  </v-content>


  <div v-if="showPopup" class="popup-overlay">
    <div class="popup-content">
      <h2>Error in the upload of the file</h2>
      <p>Please make sure you uploaded in a right way the file</p>
      <button @click="closePopup"><b>Close</b></button>
    </div>
  </div>

  <DarkModeSwitch />
</template>

<script>

import axios from 'axios';
import EventBus from '../../js/event-bus.js';
import DarkModeSwitch from '../DarkModeSwitch/DarkModeSwitch.vue';

export default {
  name: 'InputFile',
  components: {
    DarkModeSwitch
  },
  props: {
    msg: String
  },
  data() {
    return {
      chosenFiles: null,
      file_contents: null,
      showPopup: false,
      imageSrc: null,
      resultString: null
    };
  },
  computed: {
    isDarkMode() {
      return EventBus.isDarkMode.value;
    },
  },
  methods: {
    closePopup() {
      this.showPopup = false;
    },
    testFunction() {
      console.log('Select File');
    },
    importTxt() {
      let file;
      try {
        file = this.chosenFiles[0];
      } catch (e) {
        this.showPopup = true;
      }
      if (!file) {
        console.log("No File Chosen");
      } else {
        let formData = new FormData();
        formData.append('file', file);

        this.imageSrc = null;


        axios.post('http://127.0.0.1:5001/api/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
          .then(response => {
            console.log(response);
            console.log('Image Path:', 'http://127.0.0.1:5001' + response.data.image_path); // Check if the URL is correct
            this.file_contents = response.data.file_contents;
            this.imageSrc = 'http://127.0.0.1:5001' + response.data.image_path;
          })
          .catch(error => {
            console.error(error);
            this.imageSrc = null;
          });

      }
    }
  }
};



</script>

<style scoped>
/* Pop-up Style */

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  backdrop-filter: blur(5px);
  z-index: 999;
}

.popup-content {
  height: 35vh;
  width: 35vw;
  background-color: beige;
  padding: 20px;
  border-radius: 4px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.popup-content h2 {
  margin-top: 0;
}

.popup-content button {

  background-color: green;
  height: 15%;
  width: 40%;
  border-radius: 20px;
  color: black;
}


/* End of pop-up error style */


.v-content {

  height: 90vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: background-color 0.5s ease, color 0.5s ease;


}

div.v-card-text.inputContainer>div>div.v-input__prepend {
  width: 0%;
}

.darkBackground {

  background-color: rgb(255, 255, 255);
}

.lightBackground {
  background-color: rgb(59, 56, 51);
}

.outputContainer {

  height: 100%;
  width: 100%;
  display: flex;

}

v-card-title {
  text-align: center;
}

.btnContainer {

  height: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.readFileBtn {

  background-color: rgb(48, 189, 48);
  border-radius: 20px;
  width: 30%;
  height: 100%;
}

v-btn {
  height: 20%;
}

p {
  white-space: pre-wrap;
}

.inputboxlight {
  color: rgb(255, 255, 255);
}

.inputboxdark {
  color: rgb(59, 56, 51);
}

.ciao {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 0.2fr 0.8fr;
  grid-template-areas:
    "textSat"
    "imgOut"

}

.file_contents {
  grid-area: textSat;
}


.imgOutput {
  grid-area: imgOut;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.cardContainer {
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  overflow: auto;
  /* Ensures content doesn't overflow */
}

.cardText {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  overflow: auto;
  /* Ensures content doesn't overflow */
  width: 100%;
  height: 100%;
  padding: 10px;
  /* Adds some padding inside the card */
}

.imgOutput {
  max-width: 100%;
  /* Ensures image doesn't overflow */
  object-fit: contain;
}
</style>