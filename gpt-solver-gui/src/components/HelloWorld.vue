<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ msg: string }>()

  const id = "1";
  const atributes = {
    class: "hello",
    "data-storage": "11"
  }
  const display = ref(false);

const count = ref(0)
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>
  <div style="color: red;">
    <span>{{ "hello world".replace(/\s{1,}/g, "-").toUpperCase() }}</span>
  </div>
  <p :id="id" v-bind="atributes">
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
