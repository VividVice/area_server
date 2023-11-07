<template>
  <div class="dashboard">
    <img src="@/assets/logo.png" alt="Logo de mon application" class="logo">
    <h2 class="appName">Dashboard</h2>
    <p class="slogan">Connect your apps together</p>
    <router-link class="btn" to="/create-area" >Add new area</router-link>

    <h2 v-show="areas.length > 0" class="title">Your areas</h2>

    <!-- areas cards -->
    <div class="area" v-for="(area, index) in areas" :key="index">
      <div class="area-icon">
        <img :src="getIconPath(area.action_service_name)" :alt="area.action_service_name + ' Logo'" class="app-icon" style="margin-right: 10px;">
        <img :src="getIconPath(area.reaction_service_name)" :alt="area.reaction_service_name + ' Logo'" class="app-icon">
      </div>
      <div class="area-text">
        <p>{{ area.action_service_name }} in {{ area.reaction_service_name }} when {{ area.action }} do {{ area.reaction_name }}</p>
      </div>
      <div class="switch">
        <input type="checkbox" :id="'toggleSwitch' + index" checked>
        <label :for="'toggleSwitch' + index" class="slider"></label>
      </div>
    </div>
    <!-- end of areas card -->

    <!-- <h2 class="title">Recommended areas</h2>
    <div class="area">
      <div class="area-icon">
        <img src="@/assets/appIcons/spotify-icon.png" alt="Spotify Logo" class="app-icon" style="margin-right: 10px;">
        <img src="@/assets/appIcons/trello-icon.png" alt="Trello Logo" class="app-icon">
      </div>
      <div class="area-text">
        <p>Add attachment to card in Trello when new card</p>
      </div>
      <div class="area-btn">
        <button>Try it</button>
      </div>
    </div>

    <div class="area">
      <div class="area-icon">
        <img src="@/assets/appIcons/spotify-icon.png" alt="Spotify Logo" class="app-icon" style="margin-right: 10px;">
        <img src="@/assets/appIcons/trello-icon.png" alt="Trello Logo" class="app-icon">
      </div>
      <div class="area-text">
        <p>Add attachment to card in Trello when new card</p>
      </div>
      <div class="area-btn">
        <button>Try it</button>
      </div>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios';

export default {

  data() {
    return {
      serviceNames: {
        actions: [],
        reactions: []
      },
      areas: []
    };
  },
  computed: {
    token() {
      return localStorage.getItem('user-token')
    },
  },
  methods: {
    getIconPath(serviceName) {
      const icons = {
        'trello': require('@/assets/appIcons/trello-icon.png'),
        'nasa': require('@/assets/appIcons/nasa-icon.png'),
        'callr': require('@/assets/appIcons/callr-icon.png'),
        'gitHub': require('@/assets/appIcons/github-icon.png'),
        'weather': require('@/assets/appIcons/meteo-icon.png'),
        'time': require('@/assets/appIcons/timer-icon.png'),
        'spotify': require('@/assets/appIcons/spotify-icon.png'),
        'chatgpt': require('@/assets/appIcons/chatgpt-icon.png'),
      };
      return icons[serviceName] || '';
    },
    async fetchData() {
      try {
        const response = await axios.get(`http://51.20.192.77:80/Area_control`, {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${this.token}`,
          }
        });

        const data = response.data;
        const actionServiceNames = data.map(area => area.action_service_name);
        const reactionServiceNames = data.map(area => area.reaction_service_name);
        this.serviceNames.actions = actionServiceNames;
        this.serviceNames.reactions = reactionServiceNames;
        this.areas = data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
  },
  mounted() {
    this.fetchData();
  },
}
</script>

<style>

.dashboard {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding-bottom: 50px;
}

.btn {
  padding: 10px 20px;
  background-color: var(--color-complementary-1);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  text-decoration: none;
  font-family: 'Quicksand_Light', serif;
  transition: background-color 0.3s ease, transform 0.4s ease;
}

.btn:hover {
  transform: scale(1.2);
}


.logo {
  width: 150px;
}

.appName {
  margin-top: 0px;
  margin-bottom: 10px;
  font-family: 'LeagueSpartan', serif;
  font-size: 45px;
}

.slogan {
  margin-bottom: 40px;
  font-family: 'Quicksand_Light', serif;
  font-size: 20px;
}

.title {
  margin-bottom: 20px;
  font-family: 'LeagueSpartan', serif;
  font-size: 30px;
  align-self: start;
  margin-left: 25%;
}

.area {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 80%;
  font-family: 'Quicksand_Light', serif;
  max-width: 800px;
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 5px;
  background-color: #EFA7A8;
}

.area-icon {
  width: 20%;
}

.area-icon img {
  width: 20%;
}

.area-text {
  width: 60%;
}

.area-btn {
  width: 20%;
}

.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 34px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: var(--main-primary-color)
}

input:checked + .slider:before {
  transform: translateX(26px);
}

</style>