<template>
  <div class="create-area">
    <h2 class="appName2">Step 1</h2>
    <div class="dropdown">
      <h2 class="slogan">Connect this app...</h2>
      <select v-model="selectedApp1" class="dropbtn">
        <option value="" disabled selected hidden>Select app to connect</option>
        <option value="Trello">&#x1F4DD; Trello</option>
        <option value="Callr">&#x1F4DE; Callr</option>
        <!-- <option value="Time">&#x23F0; Time</option> -->
        <!-- <option value="Weather">&#x2601; Weather</option> -->
      </select>
    </div>

    <div class="dropdown">
      <h2 class="slogan">with this one!</h2>
      <select v-model="selectedApp2" class="dropbtn">
        <option value="" disabled selected hidden>Select app to connect</option>
        <option value="Trello">&#x1F4DD; Trello</option>
        <option value="ChatGPT">&#x1F4AC; ChatGPT</option>
        <option value="Callr">&#x1F4DE; Callr</option>
        <option value="Weather">&#x2601; Weather</option>
        <option value="Time">&#x23F0; Time</option>
      </select>
    </div>
  </div>

  <div class="create-area" v-show="selectedApp1 && selectedApp2">
    <h2 class="appName2">Step 2</h2>
    <div class="dropdown">
      <h2 v-if="!(selectedApp1 === 'Trello' && !trelloToken) && !(selectedApp1 === 'Callr' && !isCallrConnected)" class="slogan">When this happens...</h2>
      <select v-if="!(selectedApp1 === 'Trello' && !trelloToken) && !(selectedApp1 === 'Callr' && !isCallrConnected)" v-model="selectedAction" class="dropbtn">
        <option value="" disabled selected hidden>Select Action</option>
        <option v-if="selectedApp1 === 'Callr'" value="Call Outbound Hangup">Call Outbound Hangup</option>
        <option v-if="selectedApp1 === 'Callr'" value="Call Inbound Start">Call Inbound Start</option>
        <option v-if="selectedApp1 === 'Callr'" value="Call Outbound Start">Call Outbound Start</option>
        <option v-if="selectedApp1 === 'Callr'" value="Call Inbound Hangup">Call Inbound Hangup</option>
        <option v-if="selectedApp1 === 'Callr'" value="Media Recording">Media Recording</option>
        <option v-if="selectedApp1 === 'Callr'" value="Billing Credit">Billing Credit</option>
        <option v-if="selectedApp1 === 'Callr'" value="Send SMS">Send SMS</option>
        <option v-if="selectedApp1 === 'Callr'" value="DID Assigned">DID Assigned</option>
        <option v-if="selectedApp1 === 'Callr'" value="DID Unassigned">DID Unassigned</option>
        <!--  -->
        <option v-if="selectedApp1 === 'Trello'" value="Create Card">Create Card</option>
        <option v-if="selectedApp1 === 'Trello'" value="Create List">Create List</option>
        <option v-if="selectedApp1 === 'Trello'" value="Create Board">Create Board</option>
        <option v-if="selectedApp1 === 'Trello'" value="Create Member">Create Member</option>
        <option v-if="selectedApp1 === 'Trello'" value="Update Card">Update Card</option>
        <option v-if="selectedApp1 === 'Trello'" value="Update List">Update List</option>
        <option v-if="selectedApp1 === 'Trello'" value="Update Board">Update Board</option>
        <option v-if="selectedApp1 === 'Trello'" value="Delete Card">Delete Card</option>
        <option v-if="selectedApp1 === 'Trello'" value="Delete List">Delete List</option>
        <option v-if="selectedApp1 === 'Trello'" value="Delete Board">Delete Board</option>
        <option v-if="selectedApp1 === 'Trello'" value="Delete Member">Delete Member</option>
        <!--  -->
        <!-- <option v-if="selectedApp1 === 'Time'" value="Time">Create a Time</option> -->
        <!-- <option v-if="selectedApp1 === 'Weather'" value="Weather">Weather change</option> -->
        <!-- <option v-if="selectedApp1 === 'Weather'" value="Temperature">Temperature</option> -->
      </select>
      <button v-if="selectedApp1 === 'Trello' && !trelloToken" @click="handleTrelloLogIn">Login to Trello</button>
      <div v-if="selectedApp1 === 'Callr' && !isCallrConnected" class="input-container2">
        <h2 class="slogan">Enter your Callr credentials</h2>
        <h2 class="nameOfParam">Username</h2>
        <input class="" v-model="callrUsername" type="text" placeholder="Username">
        <h2 class="nameOfParam">Password</h2>
        <input v-model="callrPassword" type="password" placeholder="Password">
        <button style="margin-top: 20px;" @click="handleCallrLogIn">Login to Callr</button>
      </div>
    </div>

    <div class="dropdown">
      <h2 v-if="!(selectedApp2 === 'Trello' && !trelloToken) && !(selectedApp2 === 'Callr' && !isCallrConnected)" class="slogan">then do this!</h2>
      <select v-if="!(selectedApp2 === 'Trello' && !trelloToken) && !(selectedApp2 === 'Callr' && !isCallrConnected)" v-model="selectedReaction" class="dropbtn">
        <option value="" disabled selected hidden>Select Reaction</option>
        <option v-if="selectedApp2 === 'ChatGPT'" value="Post Message Sentiments">Analyse Text Sentiment</option>
        <option v-if="selectedApp2 === 'ChatGPT'" value="Post Message Categories">Create Categories From Text</option>
        <option v-if="selectedApp2 === 'ChatGPT'" value="Post Message Summarize">Summarize Text</option>
        <option v-if="selectedApp2 === 'ChatGPT'" value="Post Message Mail">Create Mail From Text</option>
        <!--  -->
        <option v-if="selectedApp2 === 'Trello'" value="Create Card">Create Card</option>
        <option v-if="selectedApp2 === 'Trello'" value="Create List">Create List</option>
        <option v-if="selectedApp2 === 'Trello'" value="Create Board">Create Board</option>
        <option v-if="selectedApp2 === 'Trello'" value="Create Member">Create Member</option>
        <option v-if="selectedApp2 === 'Trello'" value="Update Card">Update Card</option>
        <option v-if="selectedApp2 === 'Trello'" value="Update List">Update List</option>
        <option v-if="selectedApp2 === 'Trello'" value="Update Board">Update Board</option>
        <option v-if="selectedApp2 === 'Trello'" value="Delete Card">Delete Card</option>
        <option v-if="selectedApp2 === 'Trello'" value="Delete List">Delete List</option>
        <option v-if="selectedApp2 === 'Trello'" value="Delete Board">Delete Board</option>
        <option v-if="selectedApp2 === 'Trello'" value="Delete Member">Delete Member</option>
        <!--  -->
        <option v-if="selectedApp2 === 'Callr'" value="Make Call">Make Call</option>
        <option v-if="selectedApp2 === 'Callr'" value="Create Media">Create Media</option>
        <option v-if="selectedApp2 === 'Callr'" value="Get Quota Status">Get Quota Status</option>
        <option v-if="selectedApp2 === 'Callr'" value="Send SMS">Send SMS</option>
        <option v-if="selectedApp2 === 'Callr'" value="Update Media TTS">Update Media TTS</option>
        <option v-if="selectedApp2 === 'Callr'" value="Get List of Medias">Get List of Medias</option>
        <!--  -->
        <option v-if="selectedApp2 === 'Weather'" value="Get Current Weather">Get Current Weather</option>
        <!--  -->
        <option v-if="selectedApp2 === 'Time'" value="Get Current Time">Get Current Time</option>
      </select>
      <button v-if="selectedApp2 === 'Trello' && !trelloToken" @click="handleTrelloLogIn">Login to Trello</button>
      <div v-if="selectedApp2 === 'Callr' && !isCallrConnected" class="input-container2">
        <h2 class="slogan">Enter your Callr credentials</h2>
        <h2 class="nameOfParam">Username</h2>
        <input class="" v-model="callrUsername" type="text" placeholder="Username">
        <h2 class="nameOfParam">Password</h2>
        <input v-model="callrPassword" type="password" placeholder="Password">
        <button style="margin-top: 20px;" @click="handleCallrLogIn">Login to Callr</button>
      </div>
    </div>

    <div class="create-area" v-show="(selectedAction && selectedReaction) && (selectedReaction !== 'Get Quota Status' && selectedReaction !== 'Get List of Medias')">
      <h2 class="appName2" style="margin-bottom: 40px;">Step 3</h2>
      <div class="grid-container">
        <div class="grid-item">
          <!-- <h2 selectedApp1 === 'Weather'">Action Params</h2>
          <h2 v-else>ㅤ</h2>
          <div v-if="selectedApp1 === 'Time'">
            <h2 class="nameOfParam">Create a Time (in seconds)</h2>
            <p v-if="showTargetInfoAction">Insert the time in seconds</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoAction = !showTargetInfoAction">i</button>
              <input v-model="Option1app1" type="text" placeholder="Time in seconds">
            </div>
          </div>

          <div v-else-if="selectedApp1 === 'Weather'">
            <h2 class="nameOfParam">Weather</h2>
            <p v-if="showTargetInfoAction">Insert a city name and get the current weather</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoAction = !showTargetInfoAction">i</button>
              <input v-model="Option1app1" type="text" placeholder="City">
            </div>
          </div> -->
        </div>
        <div class="grid-item">
          <h2>Reaction Params</h2>

          <div v-if="selectedApp2 === 'Callr' && selectedReaction === 'Send SMS'">
            <h2 class="nameOfParam">SMS Message</h2>
            <p v-if="showMessageInfoReaction">Insert the message you want to send</p>
            <p v-if="showTargetInfoReaction">Insert the target phone number (ex: +33612345678)</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Message text">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Target">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option3app2" type="text" placeholder="Sender">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Callr' && selectedReaction === 'Make Call'">
            <h2 class="nameOfParam">Call Target</h2>
            <p v-if="showTargetInfoReaction">Insert the target phone number (ex: +33612345678)</p>
            <p v-if="showMessageInfoReaction">Insert the message you want to send</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Target">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Message">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Callr' && selectedReaction === 'Create Media'">
            <h2 class="nameOfParam">Media Name</h2>
            <p v-if="showTargetInfoReaction">Insert the name of the media</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Media name">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Callr' && selectedReaction === 'Update Media TTS'">
            <h2 class="nameOfParam">Media Name</h2>
            <p v-if="showMessageInfoReaction">Insert the id of a media callr</p>
            <p v-if="showTargetInfoReaction">Insert the name of the media</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="ID">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Media name">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Callr' && selectedReaction === 'Get List of Medias'">
            <h2 class="nameOfParam">Media Name</h2>
            <p v-if="showTargetInfoReaction">Insert the name of the media</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Media name">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Callr' && selectedReaction === 'Get Quota Status'">
          </div>

          <div v-else-if="selectedApp2 === 'Trello' && selectedReaction === 'Create Board'">
            <h2 class="nameOfParam">Board Name</h2>
            <p v-if="showTargetInfoReaction">Insert the name of the board</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Board name">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Trello' && selectedReaction === 'Create List'">
            <h2 class="nameOfParam">List Name</h2>
            <p v-if="showTargetInfoReaction">Insert the name of the list</p>
            <p v-if="showMessageInfoReaction">Insert the name of the board</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="List name">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Board name">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Trello' && selectedReaction === 'Create Card'">
            <h2 class="nameOfParam">Card Name</h2>
            <p v-if="showTargetInfoReaction">Insert the name of the card</p>
            <p v-if="showMessageInfoReaction">Insert the name of the list</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Card name">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="List name">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Trello' && selectedReaction === 'Create Member'">
            <h2 class="nameOfParam">Member Name</h2>
            <p v-if="showMessageInfoReaction">Insert the name of the board</p>
            <p v-if="showTargetInfoReaction">Insert the email of the member</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Board name">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Email">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Trello' && selectedReaction === 'Delete Board'">
            <h2 class="nameOfParam">Board Name</h2>
            <p v-if="showTargetInfoReaction">Insert the name of the board</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Board name">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Trello' && selectedReaction === 'Delete List'">
            <h2 class="nameOfParam">List id</h2>
            <p v-if="showTargetInfoReaction">Insert the name of the list</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="List id">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Trello' && selectedReaction === 'Delete Card'">
            <h2 class="nameOfParam">Card id</h2>
            <p v-if="showTargetInfoReaction">Insert the id of the card</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Card id">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Trello' && selectedReaction === 'Delete Member'">
            <h2 class="nameOfParam">Member id</h2>
            <p v-if="showTargetInfoReaction">Insert the id of the member</p>
            <p v-if="showMessageInfoReaction">Insert the name of the board</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction; showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Member id">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction; showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Board name">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Weather'">
            <h2 class="nameOfParam">Weather</h2>
            <p v-if="showTargetInfoReaction">Insert a target number and receive the current weather (ex: +33612345678)</p>
            <p v-if="showMessageInfoAction">Insert the continent + a city name and get the current weather (ex: Europe/Paris)</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoAction = !showTargetInfoAction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Target">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoAction = !showMessageInfoAction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Continent/City">
            </div>
          </div>

          <!-- chatgpt -->
          <div v-else-if="selectedApp2 === 'ChatGPT' && selectedReaction === 'Post Message Sentiments'">
            <h2 class="nameOfParam">Text Parameter</h2>
            <p v-if="showTargetInfoReaction">Insert the target number and receive the sentiment of the text (ex: +33612345678)</p>
            <p v-if="showMessageInfoReaction">Insert the text you want to analyse</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Target number">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Text">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'ChatGPT' && selectedReaction === 'Post Message Categories'">
            <h2 class="nameOfParam">Text Parameter</h2>
            <p v-if="showTargetInfoReaction">Insert the target number and receive the categories of the text (ex: +33612345678)</p>
            <p v-if="showMessageInfoReaction">Insert the text you want to analyse</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Targer number">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Text">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'ChatGPT' && selectedReaction === 'Post Message Summarize'">
            <h2 class="nameOfParam">Text Parameter</h2>
            <p v-if="showTargetInfoReaction">Insert the target number and receive the summary of the text (ex: +33612345678)</p>
            <p v-if="showMessageInfoReaction">Insert the text you want to analyse</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Target number">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Text">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'ChatGPT' && selectedReaction === 'Post Message Mail'">
            <h2 class="nameOfParam">Text Parameter</h2>
            <p v-if="showTargetInfoReaction">Insert the target number and receive the mail from the text (ex: +33612345678)</p>
            <p v-if="showMessageInfoReaction">Insert the text you want to analyse</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Target number">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="Text">
            </div>
          </div>

          <div v-else-if="selectedApp2 === 'Time' && selectedReaction === 'Get Current Time'">
            <h2 class="nameOfParam">City Parameter</h2>
            <p v-if="showTargetInfoReaction">Insert the target number and receive the time of the city (ex: +33612345678)</p>
            <p v-if="showMessageInfoReaction">Insert the city you want to know the time (ex: Paris)</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showTargetInfoReaction = !showTargetInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Target">
            </div>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option2app2" type="text" placeholder="City Name">
            </div>
          </div>

          <div v-else>
            <h2 class="nameOfParam">Text Parameter</h2>
            <p v-if="showMessageInfoReaction">Insert the text you want to send</p>
            <div class="input-container2">
              <button class="infoBtn" @click="showMessageInfoReaction = !showMessageInfoReaction">i</button>
              <input v-model="Option1app2" type="text" placeholder="Text">
            </div>
          </div>
        </div>
      </div>
    </div>


    <p>
      <span :class="{ 'selected': selectedApp1 }">{{ selectedApp1 }}</span>
      in
      <span :class="{ 'selected': selectedApp2 }">{{ selectedApp2 }}</span>
      when
      <span :class="{ 'selected': selectedAction }">{{ selectedAction }}</span>
      do
      <span :class="{ 'selected': selectedReaction }">{{ selectedReaction }}</span>
    </p>

    <button style="margin-bottom: 40px;" @click="handleTryItClick">Try it</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreateArea',
  computed: {
    token() {
      return localStorage.getItem('user-token')
    }
  },
  async mounted() {
    const current = document.URL;
    this.trelloToken = current.split('#token=')[1];
    if (this.trelloToken) {
      try {
        const response = await axios.get(
          `http://51.20.135.59:80/trello/?access_token=${this.trelloToken}`,
          {
            headers: {
              Application: 'application/json',
              Authorization: `Bearer ${this.token}`,
            },
          }
        );
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }
    this.selectedApp1 = localStorage.getItem('selectedApp1') || '';
    this.selectedApp2 = localStorage.getItem('selectedApp2') || '';
  },
  data() {
    return {
      selectedApp1: '',
      selectedApp2: '',
      // options: [
      //   { value: 'Trello', name: 'Trello', icon: 'web/src/assets/appIcons/trello-icon.png' },
      //   { value: 'Callr', name: 'Callr', icon: 'web/src/assets/appIcons/callr-icon.png' },
      //   { value: 'Time', name: 'Time', icon: 'web/src/assets/appIcons/time-icon.png' },
      //   { value: 'Weather', name: 'Weather', icon: 'web/src/assets/appIcons/meteo-icon.png' },
      // ],
      selectedAction: '',
      selectedReaction: '',
      trelloToken: '',
      Option1app1: '',
      Option2app1: '',
      reaction_param: {},
      Option1app2: '',
      Option2app2: '',
      Option3app2: '',
      showMessageInfoAction: false,
      showTargetInfoAction: false,
      showMessageInfoReaction: false,
      showTargetInfoReaction: false,
      callrUsername: '',
      callrPassword: '',
      isCallrConnected: false,
    };
  },
  methods: {
    toCamelCase(str) {
      return str
        .split(' ')
        .map((word, index) =>
          index === 0 ? word.toLowerCase() : word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
        )
        .join('');
    },
    async handleTrelloLogIn() {
      try {
        const response = await axios.post(
          `http://51.20.135.59:80/subscribe`,
          {
            service: "trello",
            service_args: {
              return_url: "http://localhost:8081/create-area",
            },
          },
          {
            timeout: 10000,
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${this.token}`,
            },
          }
        );
        if (response.status === 200) {
          this.redirectUrl = response.data.auth_url;
          document.location.replace(this.redirectUrl);
        } else if (response.status === 201) {
          this.trelloToken = "true"
          console.log('Trello already connected');
        } else {
          alert("Trello connection failed");
        }
      } catch (error) {
        console.error(error);
      }
    },
    async handleCallrLogIn() {
      if (!this.callrUsername || !this.callrPassword) {
        alert('Please enter your Callr credentials');
        return;
      }
      try {
        const response = await axios.post(
          `http://51.20.135.59:80/subscribe`,
          {
            service: "callr",
            service_args: {
              username: this.callrUsername,
              password: this.callrPassword,
            },
          },
          {
            timeout: 10000,
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${this.token}`,
            },
          }
        );
        if (response.status === 200) {
          this.isCallrConnected = true;
        } else if (response.status === 201) {
          this.isCallrConnected = true;
          console.log('Callr already connected');
        } else {
          alert("Callr connection failed");
        }
      } catch (error) {
        alert("Callr connection failed");
        console.error(error);
      }
    },
    setActionParams() {
      let action_p = {};
      // if (this.selectedApp1 === 'Time') {
      //   if (this.selectedAction === 'Get Current Time') {
      //     action_p = {
      //       hour: this.Option1app1,
      //       minute: this.Option2app1,
      //     };
      //   }
      // }
      // if (this.selectedApp1 === 'Weather') {
      //   if (this.selectedAction === 'Temperature') {
      //     action_p = {
      //       temperature: this.Option1app1,
      //     };
      //   }
      // }
      return action_p;
    },
    setReactionParams() {
      let reaction_p = {};
      if (this.selectedApp2 === 'Trello') {
        if (this.selectedReaction === 'Create Card') {
          reaction_p = {
            board_name: this.Option1app2,
            list_name: this.Option2app2,
            card_name: this.Option3app2,
          };
        }
        if (this.selectedReaction === 'Create Board') {
          reaction_p = {
            name: this.Option1app2,
          };
        }
        if (this.selectedReaction === 'Create List') {
          reaction_p = {
            name: this.Option1app2,
            board_name: this.Option2app2,
          };
        }
        if (this.selectedReaction === 'Delete Board') {
          reaction_p = {
            name: this.Option1app2,
          };
        }
        if (this.selectedReaction === 'Delete List') {
          reaction_p = {
            id: this.Option1app2,
          };
        }
        if (this.selectedReaction === 'Delete Card') {
          reaction_p = {
            id: this.Option1app2,
          };
        }
        if (this.selectedReaction === 'Create Member') {
          reaction_p = {
            name: this.Option1app2,
            email: this.Option2app2,
          };
        }
        if (this.selectedReaction === 'Delete Member') {
          reaction_p = {
            board_name: this.Option1app2,
            email: this.Option2app2,
          };
        }
        if (this.selectedReaction === 'Update Board') {
          reaction_p = {
            name: this.Option1app2,
            new_name: this.Option2app2,
          };
        }
        if (this.selectedReaction === 'Update List') {
          reaction_p = {
            board_name: this.Option1app2,
            list_name: this.Option2app2,
            new_name: this.Option3app2,
          };
        }
        if (this.selectedReaction === 'Update Card') {
          reaction_p = {
            board_name: this.Option1app2,
            card_name: this.Option2app2,
            new_name: this.Option3app2,
          };
        }
      }

      if (this.selectedApp2 === 'Callr') {
        if (this.selectedReaction === 'Make Call') {
          reaction_p = {
            target: this.Option1app2,
            msg: this.Option2app2,
          };
        }
        if (this.selectedReaction === 'Send Sms') {
          reaction_p = {
            target: this.Option1app2,
            msg: this.Option2app2,
            sender: this.Option3app2,
          };
        }
        if (this.selectedReaction === 'Create Media') {
          reaction_p = {
            name: this.Option1app2,
          };
        }
        if (this.selectedReaction === 'Update Media TTS') {
          reaction_p = {
            id: this.Option1app2,
            msg: this.Option2app2,
          };
        }
        if (this.selectedReaction === 'Get List of Medias') {
          reaction_p = {};
        }
        if (this.selectedReaction === 'Get Quota Status') {
          reaction_p = {};
        }
      }

      if (this.selectedApp2 === 'ChatGPT') {
        if (this.selectedReaction === 'Post Message Sentiments') {
          reaction_p = {
            target: this.Option1app2,
            message_content: this.Option2app2,
          };
        }
        if (this.selectedReaction === 'Post Message Categories') {
          reaction_p = {
            target: this.Option1app2,
            message_content: this.Option2app2,
          };
        }
        if (this.selectedReaction === 'Post Message Summarize') {
          reaction_p = {
            target: this.Option1app2,
            message_content: this.Option2app2,
          };
        }
        if (this.selectedReaction === 'Post Message Mail') {
          reaction_p = {
            target: this.Option1app2,
            message_content: this.Option2app2,
          };
        }
      }

      if (this.selectedApp2 === 'Weather') {
        if (this.selectedReaction === 'Get Current Weather') {
          reaction_p = {
            target: this.Option1app2,
            city: this.Option2app2,
          };
        }
      }

      if (this.selectedApp2 === 'Time') {
        if (this.selectedReaction === 'Get Current Time') {
          reaction_p = {
            target: this.Option1app2,
            city: this.Option2app2,
          };
        }
      }
      return reaction_p;
    },
    formatAction(action) {
      if (this.selectedApp1 === 'Callr' && action === 'Call Outbound Hangup') {
        return 'call.outbound_hangup';
      } else if (this.selectedApp1 === 'Callr' && action === 'Call Inbound Start') {
        return 'call.inbound_start';
      } else if (this.selectedApp1 === 'Callr' && action === 'Call Outbound Start') {
        return 'call.outbound_start';
      } else if (this.selectedApp1 === 'Callr' && action === 'Call Inbound Hangup') {
        return 'call.inbound_hangup';
      } else if (this.selectedApp1 === 'Callr' && action === 'Media Recording') {
        return 'media.recording.new';
      } else if (this.selectedApp1 === 'Callr' && action === 'Billing Credit') {
        return 'billing.credit';
      } else if (this.selectedApp1 === 'Callr' && action === 'Send SMS') {
        return 'sms.mo';
      } else if (this.selectedApp1 === 'Callr' && action === 'DID Assigned') {
        return 'did.assigned';
      } else if (this.selectedApp1 === 'Callr' && action === 'DID Unassigned') {
        return 'did.unassigned';
      } else {
        return this.toCamelCase(action);
      }
    },
    async handleTryItClick() {
      if (!this.selectedApp1 || !this.selectedApp2 || !this.selectedAction || !this.selectedReaction) {
        alert('Please select all the fields');
        return;
      }
      localStorage.setItem('selectedApp1', this.selectedApp1);
      localStorage.setItem('selectedApp2', this.selectedApp2);

      const body = {
        action_service: this.toCamelCase(this.selectedApp1),
        action_name: this.formatAction(this.selectedAction),
        action_params: this.setActionParams(),
        reaction_service: this.toCamelCase(this.selectedApp2),
        reaction_name: this.toCamelCase(this.selectedReaction),
        reaction_params: this.setReactionParams(),
      };
      console.log(body);

      try {
        const response = await fetch('http://51.20.135.59:80/create_AREA', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${this.token}`
          },
          body: JSON.stringify(body)
        });
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error('Error:', error);
      }
    },
  }
};
</script>

<style>
.create-area {
  margin: 0 auto;
  width: 80%;
  max-width: 800px;
  text-align: center;
}

.app-icon {
  width: 20px;
  margin-right: 10px;
}

.dropdown {
  position: relative;
  display: inline-block;
  margin: 10%;
}

.dropbtn {
  background-color: var(--color-complementary-1);
  color: white;
  padding: 16px;
  font-size: 16px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  width: 220px;
}

.appName2 {
  margin-top: 40px;
  margin-bottom: 0px;
  font-family: 'LeagueSpartan', serif;
  font-size: 45px;
  color: white;
}

.dropdown-content {
  display: none;
  position: absolute;
  z-index: 1;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  padding: 12px 16px;
  margin-top: 5px;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.input-container2 {
  position: relative;
  margin-bottom: 15px;
}

.input-container2 input {
  padding-left: 40px;
  padding: 10px;
  width: 60%;
  border-radius: 5px;
  font-size: 16px;
  font-family: 'LeagueSpartan', serif;
  background-color: white;
}

.input-container2 .icon {
  position: absolute;
  left: 37%;
  top: 50%;
  transform: translateY(-50%);
  color: var(--main-primary-color);
}

.infoBtn {
  position: absolute;
  left: 0%;
  top: 10%;
  color: var(--main-primary-color);
  background-color: white;
  margin-right: 20px;
  border: none;
  border-radius: 50%;
  font-size: 12px;
  cursor: pointer;
}

.show {
  display: block;
}

.selected {
  color: var(--color-complementary-1);
}

.nameOfParam {
  margin-bottom: 40px;
  font-family: 'Quicksand_Light', serif;
  font-size: 20px;
  color: var(--color-complementary-1);
}

.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

</style>