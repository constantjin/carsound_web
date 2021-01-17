<template>
  <div>
    <p class="text-2xl">Arousal (자극적임)</p>
    <div class="grid grid-cols-9 gap-x-2.5 mt-5">
      <div
        class="text-2xl text-bold border-2 rounded-md px-1.5 text-center"
        v-for="(n, idx) in 9"
        :key="idx"
        @click="setArousal(n)"
        :class="arousal_style[idx]"
      >
        {{ n }}
      </div>
      <div class="col-start-1 col-span-2 text-sm mt-2">← 덜 자극적임</div>
      <div class="col-start-8 col-span-2 text-sm mt-2">더 자극적임 →</div>
    </div>
  </div>

  <div class="mt-8">
    <p class="text-2xl">Dominance (지배적임)</p>
    <div class="grid grid-cols-9 gap-x-2.5 mt-5">
      <div
        class="text-2xl text-bold border-2 rounded-md px-1.5 text-center"
        v-for="(n, idx) in 9"
        :key="idx"
        @click="setDominance(n)"
        :class="dominance_style[idx]"
      >
        {{ n }}
      </div>
      <div class="col-start-1 col-span-2 text-sm mt-2 text-left">
        ← 더 지배되는
      </div>
      <div class="col-start-8 col-span-2 text-sm mt-2 text-center">
        더 지배하는 →
      </div>
    </div>

    <div class="mt-8">
      <p class="text-2xl">Valence (감정가)</p>
      <div class="grid grid-cols-9 gap-x-2.5 mt-5">
        <div
          class="text-2xl text-bold border-2 rounded-md px-1.5 text-center"
          v-for="(n, idx) in 9"
          :key="idx"
          @click="setValence(n)"
          :class="valence_style[idx]"
        >
          {{ n }}
        </div>
        <div class="col-start-1 col-span-2 text-sm mt-2 text-left">
          ← 불쾌한 감정
        </div>
        <div class="col-start-8 col-span-2 text-sm mt-2 text-center">
          유쾌한 감정 →
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, computed, onMounted, watch } from "vue";
import { useRouter } from "vue-router";

import useExperiment from "../hooks/useExperiment";

const router = useRouter();
const { sendRating } = useExperiment();

const ratings = reactive({
  arousal: 0,
  dominance: 0,
  valence: 0,
});
const arousal_style = ref([]);
const dominance_style = ref([]);
const valence_style = ref([]);
const timeover = ref(false);

const setArousal = (val) => {
  arousal_style.value = [];
  arousal_style.value[val - 1] = "border-red-500";
  ratings.arousal = val;
};
const setDominance = (val) => {
  dominance_style.value = [];
  dominance_style.value[val - 1] = "border-red-500";
  ratings.dominance = val;
};
const setValence = (val) => {
  valence_style.value = [];
  valence_style.value[val - 1] = "border-red-500";
  ratings.valence = val;
};

const submitRatings = async () => {
  await sendRating(ratings);
  router.push("/emotional");
};

watch(
  () => {
    return (
      ratings.arousal !== 0 && ratings.dominance !== 0 && ratings.valence !== 0
    );
  },
  async (curr, prev) => {
    if (curr === true) {
      await submitRatings();
    }
  }
);

watch(
  () => {
    return timeover.value;
  },
  async (curr, prev) => {
    if (curr === true) {
      await submitRatings();
    }
  }
);

// watchEffect(async () => {
//   const rating_finished =
//     ratings.arousal !== 0 && ratings.dominance !== 0 && ratings.valence !== 0;
//   if (rating_finished || timeover) {
//     await sendRating(ratings);
//     router.push("/emotional");
//   }
// });

onMounted(() => {
  setTimeout(() => {
    timeover.value = true;
  }, 10000);
});
</script>

<style scoped></style>
