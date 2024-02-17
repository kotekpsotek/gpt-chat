<script setup lang="ts">
    import General from './components/General.vue';
    import HelloWorld from './components/HelloWorld.vue';
    import QuestionList from './components/QuestionList.vue';

    import { ref } from 'vue';
    import APIStorage from "./api";
    
    let api = "http://localhost:5454";

    const questions = ref(APIStorage.getStorageQuestions());
</script>

<template>
  <!-- <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" /> -->
  <div class="flex h-screen w-screen justify-center items-center">
    <General v-bind:api="api"/>
    <QuestionList :questions="questions"/>
  </div>

  <!-- <HelloWorld msg="Hello"/> -->
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
