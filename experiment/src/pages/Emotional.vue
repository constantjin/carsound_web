<template>
  <div>
    <p class="text-7xl">+</p>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import useHowler from "../hooks/useHowler";

const router = useRouter();
const {
  playEmotionalSound,
  pauseBaseSound,
  stopRunSound,
  destroyBaseSound,
  destroyRunSound,
  destroyEmotionalSound,
} = useHowler();

onMounted(async () => {
  await playEmotionalSound();
  pauseBaseSound();
  stopRunSound();
  console.log("TODO: route to rating page");
});
</script>

<style scoped></style>
