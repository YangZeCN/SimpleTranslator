<script setup lang="ts">
import TranslatorApp from './components/TranslatorApp.vue'; 
</script>

<template>
  <div class="layout">
    <TranslatorApp />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.layout {
  display: flex;
  height: 100vh;
}
</style>
