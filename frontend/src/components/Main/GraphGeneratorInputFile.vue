<!-- create a toolbar in vue with an input for a file -->
<template>
    <v-content class="v-content">
      <v-container fill-height>
        <v-row style="margin: 0" justify="center">
          <v-col cols="auto">
            <v-card class="v-card" raised>
              <v-card-title><b>Graph Generator</b></v-card-title>
              <br>
              <v-card-text class="inputContainer">                
                <div class="inputGroupContainer">
                  <div id="NodesNumberContainer">
                    <input type="text" id="NodesNumberInput" v-model="textInput" placeholder="Number of Nodes"/>
                  </div>
                  <div id="EdgesNumberContainer">
                    <input type="text" id="EdgesNumberInput" v-model="textInput" placeholder="Number of Edges"/>
                  </div>
                  <div id="FileNameContainer">
                    <input type="text" id="FileNameInput" v-model="textInput" placeholder="File Name"/>
                  </div>
                  <div id="Hamiltonian">
                    <label>
                      <input type="checkbox" v-model="isCheckedA" @change="handleCheckboxChange('A')" />
                      <b>Hamiltonian Cycle</b>
                    </label>
                  </div>
                  <div id="Random">
                    <label>
                      <input type="checkbox" v-model="isCheckedB" @change="handleCheckboxChange('B')" />
                      <b>Random</b>
                    </label>
                  </div>
                </div>
              </v-card-text>
              <v-card-actions class="btnContainer">
                <v-btn right class="readFileBtn" @click="UploadInfo"><b>Read File</b></v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col cols="auto">
            <v-card width="45vw" height="40vh" raised>
              <v-card-title><b>File contents:</b></v-card-title>
              <v-card-text><p>{{file_content}}</p></v-card-text>
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

</template>

<script>
export default {
  name: 'GraphGeneratorInputFile',
  props: {
    msg: String
  },
  data () {
    return {
      chosenFiles: null,
      file_content: null,
      showPopup: false,
      isCheckedA: false,
      isCheckedB: false
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
      console.log('importTxt');
      // console.log(this.chosenFiles[0]);
      let file;
      try {
        file = this.chosenFiles[0]
      } catch (e) {
        this.showPopup = true;
      }
      if (!file) {console.log("No File Chosen")}
      else {
        let reader = new FileReader();
        // Use the javascript reader object to load the contents of the file in the v-model prop
        reader.onload = (res) => {
          this.file_content = res.target.result;
          console.log("content", this.file_content);
        };
        reader.onerror = (err) => console.log(err);
        reader.readAsText(file);
        // console.log("readre", reader);
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

p {
  white-space: pre-wrap;
}
</style>