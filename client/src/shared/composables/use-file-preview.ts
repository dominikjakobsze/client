import { ref, onUnmounted, toValue } from 'vue'
import type { UseFilePreviewOptions } from '@/shared/types/file-preview.types'
import { validateFile, FILE_VALIDATION_MESSAGES } from '@/shared/services/file-preview.service'

export function useFilePreview(options: UseFilePreviewOptions) {
  const previewUrl = ref<string | null>(null)
  const errorMessage = ref<string | null>(null)

  const reset = (): void => {
    if (previewUrl.value) {
      URL.revokeObjectURL(previewUrl.value)
      previewUrl.value = null
    }
    errorMessage.value = null
  }

  const setFile = (file: File | undefined): void => {
    if (!file) return

    const errorType = validateFile(file, {
      maxSize: toValue(options.maxSize),
      allowedTypes: toValue(options.allowedTypes),
    })

    reset()

    if (errorType) {
      errorMessage.value = FILE_VALIDATION_MESSAGES[errorType]
      return
    }

    previewUrl.value = URL.createObjectURL(file)
  }

  onUnmounted(reset)

  return {
    previewUrl,
    errorMessage,
    setFile,
    reset,
  }
}
