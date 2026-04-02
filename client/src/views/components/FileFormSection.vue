<script setup lang="ts">
import { ImagePlus } from 'lucide-vue-next'
import { useFilePreview } from '@/composables/useFilePreview'

const MAX_SIZE_BYTES = 10 * 1024 * 1024
const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp']

const { previewUrl, errorMessage, setFile } = useFilePreview({
  maxSize: MAX_SIZE_BYTES,
  allowedTypes: ALLOWED_TYPES,
})

const handleFileChange = (e: Event) => {
  const target = e.target as HTMLInputElement
  setFile(target.files?.[0])

  target.value = ''
}
</script>

<template>
  <form
    class="group animate-smooth isolate mx-auto mt-10 grid w-full max-w-9/10 flex-none grid-cols-1 grid-rows-1 overflow-hidden rounded-4xl border-2 border-dashed border-neutral-400 bg-neutral-50 hover:border-blue-700 lg:max-w-250"
    @submit.prevent
  >
    <!-- Sekcja podglądu -->
    <div
      class="animate-smooth z-1 col-start-1 row-start-1 aspect-3/4 w-full group-hover:scale-105 sm:aspect-2/1"
    >
      <img
        v-if="previewUrl"
        :src="previewUrl"
        alt="Uploaded preview"
        class="h-full w-full object-cover"
      />
    </div>

    <!-- Overlay dla podglądu -->
    <div v-if="previewUrl" class="z-2 col-start-1 row-start-1 bg-neutral-900/30" />

    <!-- Interfejs użytkownika -->
    <div
      class="z-3 col-start-1 row-start-1 flex max-w-[45rch] flex-none flex-col gap-2 self-center justify-self-center p-4 text-center text-neutral-800"
    >
      <label
        class="animate-smooth flex aspect-square w-15 flex-none cursor-pointer flex-col items-center justify-center self-center overflow-hidden rounded-full bg-blue-50 hover:scale-110"
      >
        <ImagePlus class="h-8 w-8 flex-none text-blue-700" />
        <input
          type="file"
          class="sr-only"
          accept="image/jpeg,image/png,image/webp"
          @change="handleFileChange"
        />
      </label>

      <h3
        class="flex-none text-2xl leading-tight font-semibold"
        :class="{ 'text-neutral-50': previewUrl }"
      >
        Identify a new species
      </h3>

      <p class="min-h-[2.5rlh] flex-none leading-normal" :class="{ 'text-neutral-50': previewUrl }">
        <span
          v-if="errorMessage"
          class="font-medium text-blue-700"
          :class="{ 'text-red-400': previewUrl }"
        >
          {{ errorMessage }}
        </span>
        <span v-else>
          Select your image and hit the button below to find out what animal it is
        </span>
      </p>

      <button
        type="submit"
        class="animate-smooth w-fit flex-none cursor-pointer self-center rounded-4xl border-2 border-blue-700 bg-blue-700 px-8 py-3 leading-normal font-semibold text-neutral-50 shadow-lg hover:bg-neutral-50 hover:text-blue-700 active:scale-95"
      >
        Analyse
      </button>
    </div>
  </form>
</template>

<style scoped></style>
