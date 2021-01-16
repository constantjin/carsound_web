<template>
  <div>
    <alert />
    <keep-alive>
      <sound />
    </keep-alive>
    <div
      id="app"
      class="min-h-screen flex flex-col justify-center items-center text-center m-auto"
    >
      <router-view />
    </div>
  </div>
</template>

<script setup>
import Alert from "./components/Alert.vue";
import Sound from "./components/Sound.vue";
</script>

<style scoped></style>
