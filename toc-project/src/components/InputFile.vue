<!-- create a toolbar in vue with an input for a file -->
<template>
    <v-content>
      <v-container fill-height>
        <v-row justify="center">
          <v-col cols="auto">
            <v-card width="600" height="300" raised>
              <v-card-title>Vuetify v-file-input Example:</v-card-title>
              <br>
              <v-card-text>                
                <v-file-input
                  accept=".txt"
                  label="Click here to select a .txt file"
                  outlined
                  v-model="chosenFile"
                  v-on:click="testFunction"
                >
                </v-file-input>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn right @click="importTxt">Read File</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col cols="auto">
            <v-card width="600" height="300" raised>
              <v-card-title>File contents:</v-card-title>
              <v-card-text><p>{{ chosenFile }}</p></v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
</template>

<script>

export default {
  name: 'InputFile',
  props: {
    msg: String
  },
  data () {
    return {
      chosenFile: null, // <- initialize the v-model prop
      // data: null
    }
  },
  methods: {
    testFunction() {
      console.log('Select File');
    },
    importTxt() {
      console.log('importTxt');
      console.log(this.chosenFile);
      // console.log(this.$refs.file.files[0]);
      // if (!this.chosenFile) {this.data = "No File Chosen"}
      // let reader = new FileReader();
      // Use the javascript reader object to load the contents
      // of the file in the v-model prop
      // reader.readAsText(this.chosenFile);
      // reader.onload = () => {
      //   this.data = reader.result;
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
</script>

<style scoped>
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

p {
  white-space: pre-wrap;
}
</style>