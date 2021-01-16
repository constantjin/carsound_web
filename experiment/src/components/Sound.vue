<template>
  <div></div>
</template>

<script setup>
import { reactive } from "vue";
import useHowler from "../hooks/useHowler";

const { base_sound, run_sound, emotional_sound } = useHowler();
</script>

<style scoped></style>
