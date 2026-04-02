<script setup lang="ts">
import { Proportions } from 'lucide-vue-next'
import { ref } from 'vue'

const imageAspect = ref<boolean>(false)
const onClickChangeImageScale = () => {
  imageAspect.value = !imageAspect.value
}
</script>

<template>
  <article
    class="isolate mx-auto mt-10 grid w-full max-w-9/10 flex-none grid-cols-1 grid-rows-1 overflow-hidden rounded-4xl lg:max-w-300"
  >
    <div class="z-2 col-start-1 row-start-1 aspect-3/4 w-full bg-neutral-100 sm:aspect-2/1">
      <img
        src="https://picsum.photos/800/1200"
        alt="Uploaded preview"
        class="h-full w-full"
        :class="{ 'object-cover': !imageAspect, 'object-contain': imageAspect }"
      />
    </div>

    <div
      class="overlay-gradient z-3 col-start-1 row-start-1 flex w-full flex-col gap-5 self-end justify-self-start p-5 sm:p-10"
    >
      <p
        class="flex-none self-center rounded-full border-2 border-zinc-500 bg-zinc-600 px-3 py-1 text-xs leading-normal font-medium tracking-wide text-slate-50 sm:self-start sm:px-5 sm:py-2"
      >
        CONFIDENCE SCORE <span class="font-bold">98%</span>
      </p>
      <div class="flex w-full flex-none items-center justify-start gap-2">
        <h3 class="flex-initial text-4xl font-bold text-slate-50 sm:text-7xl">Golden Retriever</h3>
        <Proportions
          class="animate-smooth ml-auto h-7 w-7 flex-none cursor-pointer text-slate-50 hover:scale-110 active:scale-90 sm:h-10 sm:w-10"
          @click="onClickChangeImageScale"
        />
      </div>
    </div>
  </article>
</template>

<style scoped></style>
