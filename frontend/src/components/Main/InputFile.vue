<!-- create a toolbar in vue with an input for a file -->
<template>
    <v-content class="v-content">
      <v-container fill-height>
        <v-row style="margin: 0" justify="center">
          <v-col cols="auto">
            <v-card width="45vw" height="40vh" raised>
              <v-card-title>Vuetify v-file-input Example:</v-card-title>
              <br>
              <v-card-text class="inputContainer">                
                <v-file-input
                  accept=".txt"
                  label="Click here to select a .txt file"
                  outlined
                  v-model="chosenFiles"
                  v-on:click="testFunction"
                >
                </v-file-input>
              </v-card-text>
              <v-card-actions class="btnContainer">
                <v-btn right class="readFileBtn" @click="importTxt"><b>Read File</b></v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col cols="auto">
            <v-card width="45vw" height="40vh" raised>
              <v-card-title>File contents:</v-card-title>
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
  name: 'InputFile',
  props: {
    msg: String
  },
  data () {
    return {
      chosenFiles: null,
      file_content: null,
      showPopup: false,
    };
  },
  methods: {
    closePopup() {
      this.showPopup = false;
    },
    testFunction() {
      console.log('Select File');
    },
    importTxt() {
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


.inputContainer { 
  
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

  height: 30%;
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