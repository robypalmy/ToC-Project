<!-- create a toolbar in vue with an input for a file -->
<template>
  <v-content :class="{ 'dark-mode': isDarkMode, 'light-mode': !isDarkMode }" class="v-content">
    <v-container fill-height>
      <v-row style="margin: 0" justify="center">
        <v-col cols="auto">
          <v-card :class="{ 'lightBackground': isDarkMode, 'darkBackground': !isDarkMode }" class="v-card" raised>
            <v-card-title :class="{ 'white-text': isDarkMode, 'black-text': !isDarkMode }"><b>Graph Generator</b></v-card-title>
            <br>
            <v-card-text class="inputContainer">                
              <div class="inputGroupContainer">
                <div id="NodesNumberContainer">
                  <input type="text" id="NodesNumberInput" v-model="NodesInput" placeholder="Number of Nodes"/>
                </div>
                <div id="EdgesNumberContainer">
                  <input type="text" id="EdgesNumberInput" v-model="EdgesInput" placeholder="Number of Edges"/>
                </div>
                <div id="FileNameContainer">
                  <input type="text" style="color:black" id="FileNameInput" v-model="FileNameInput" placeholder="File Name"/>
                </div>
                <div id="Hamiltonian">
                  <label id="label">
                    <input type="checkbox"  v-model="isCheckedA" @change="handleCheckboxChange('A')" />
                    <b :class="{ 'white-text': isDarkMode, 'black-text': !isDarkMode }">Hamiltonian Cycle</b>
                  </label>
                </div>
                <div id="Random">
                  <label id="label">
                    <input type="checkbox" v-model="isCheckedB" @change="handleCheckboxChange('B')" />
                    <b :class="{ 'white-text': isDarkMode, 'black-text': !isDarkMode }" >Random</b>
                  </label>
                </div>
              </div>
            </v-card-text>
            <v-card-actions class="btnContainer">
              <v-btn right class="readFileBtn" @click="UploadInfo"><b>Generate File</b></v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="auto">
          <v-card :class="{ 'lightBackground': isDarkMode, 'darkBackground': !isDarkMode }" width="45vw" height="41vh" raised>
            <v-card-title :class="{ 'white-text': isDarkMode, 'black-text': !isDarkMode }" ><b>File contents:</b></v-card-title>
            <v-card-text :class="{ 'white-text': isDarkMode, 'black-text': !isDarkMode }"><p>{{file_contents}}</p></v-card-text>
            <img class="imgOutput" style="max-height: 300px" :src="imageSrc" :key="imageSrc" alt="Image from backend"
                v-if="imageSrc" />
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

  <DarkModeSwitch/>

</template>

<script>
import axios from 'axios';
import EventBus from '../../js/event-bus.js';
import DarkModeSwitch from '../DarkModeSwitch/DarkModeSwitch.vue';
export default {
name: 'GraphGeneratorInputFile',
components: {
  DarkModeSwitch
},
props: {
  msg: String
},
computed: {
    isDarkMode() {
      return EventBus.isDarkMode.value;
    },
  },
data () {
  return {
    file_contents: null,
    imageSrc: null,
    showPopup: false,
    isCheckedA: false,
    isCheckedB: false,
    NodesInput: null,
    EdgesInput: null,
    FileNameInput: null,
  };
},
methods: {
  handleCheckboxChange(checkbox) {
    if (checkbox === 'A') {
      this.isCheckedB = false; // Uncheck Option B if Option A is selected
    } else if (checkbox === 'B') {
      this.isCheckedA = false; // Uncheck Option A if Option B is selected
    }
  },
  closePopup() {
    this.showPopup = false;
  },
  testFunction() {
    console.log('Select File');
  },
  UploadInfo() {
    console.log('UploadInfo');
    let nodes = parseInt(this.NodesInput)
    let edges = parseInt(this.EdgesInput)
    let fileName = this.FileNameInput + ".txt"
    let hamiltonian = this.isCheckedA
    let random = this.isCheckedB
    console.log(nodes, edges, fileName, hamiltonian, random)
    if (nodes && edges && fileName && (hamiltonian || random)) {
      console.log("All good")
      let formData = {
        'nodes': nodes,
        'edges': edges,
        'fileName': fileName,
        'hamiltonian': hamiltonian,
        'random': random,
      }
      axios.post('http://127.0.0.1:5001/api/generate', formData, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => {
        console.log(response.data);
        this.file_contents = response.data.file_contents;
        this.imageSrc = 'http://127.0.0.1:5001' + response.data.image_path; 
        // Handle the response from the Flask backend
      })
      .catch(error => {
        console.error(error);
        // Handle any errors that occurred during the request
      });
            
    } else {
      this.showPopup = true;
    }
  },
  mounted() {
    console.log('mounted');
    console.log(this.$refs.file);
  },
  created() {
    console.log('created');
    console.log(this.$refs.file);
  }
}
} 
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

#label {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap:20px;
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
color: black;}


/* End of pop-up error style */


.v-content {

height: 90vh;
width: 100%;
display: flex;
flex-direction: column;
align-items: center;


}


.v-card-title {

width:100%;
text-align:center;
font-size: 1.5em;

}


.v-card {

width: 45vw;
height: 40vh;
display: flex;
flex-direction: column;
justify-content: space-around;
align-items: center;


}



.inputContainer { 

height: 100%;
width: 40vw;
display: flex;
align-items: center;
padding: 0;
justify-content: center;

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
.inputGroupContainer {
width: 40vw;
height: 100%;
display: grid;
grid-template-columns: 1fr 1fr;
grid-gap: 10px;
grid-template-rows: 1fr 1fr 1fr;
grid-template-areas: 
  "NodeNumberInput EdgeNumberInput"
  "FileNameInput FileNameInput"
  "HamiltonianInput RandomInput";
}

#NodesNumberContainer {
grid-area: NodeNumberInput;
display: flex;
align-items: center;
justify-content: center;
text-align: center;
}

#EdgesNumberContainer {
grid-area: EdgeNumberInput;
display: flex;
align-items: center;
justify-content: center;
text-align: center;
}

#FileNameContainer {
grid-area: FileNameInput;
display: flex;
align-items: center;
justify-content: center;
text-align: center;
}

#NodesNumberInput, #EdgesNumberInput {

display: flex;
border-radius: 5%;
background-color: rgb(234, 233, 233);
text-align: center;
width: 80%;
height: 90%;
font-size: 1.2em;
font-weight: bold;
color: black;
}

#FileNameInput {

display: flex;
border-radius: 5%;
background-color: rgb(234, 233, 233);
text-align: center;
width: 90%;
height: 90%;
font-size: 1.2em;
font-weight: bold;
}

#Hamiltonian {
grid-area: HamiltonianInput;
/* background-color: rgb(234, 233, 233); */

}

#Random {
grid-area: RandomInput;
/* background-color: rgb(234, 233, 233); */

}

#Hamiltonian , #Random {
border-radius: 10%;
display: flex;
align-items: center;
justify-content: center;
text-align: center;
width: 100%;
height: 100%;
font-size: 1.2em;
}



.file-card {
margin: 20px;
padding: 20px;
}

.card-title {
font-size: 20px;
font-weight: bold;
}

.read-btn {
color: white;
background-color: #1976d2;
}

.btnContainer {

height: 20%;
width: 45vw;
display: flex;
justify-content: center;
align-items: center;
}

.readFileBtn {

background-color: rgb(48, 189, 48);
border-radius: 20px;
width: 30%;
height: 40px;
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
  grid-template-rows: 0.2fr 0.7fr;
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