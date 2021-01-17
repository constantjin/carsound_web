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
  destroyEmotionalSound();
  router.push("/rating");
});
</script>

<style scoped></style>
