import { ref, onUnmounted, toValue, type MaybeRefOrGetter } from 'vue'

export type FileValidationError = 'NOT_A_FILE' | 'TOO_BIG' | 'UNSUPPORTED_FORMAT'

export interface FileValidatorConfig {
  maxSize: number
  allowedTypes: string[]
}

// -- WARSTWA AGNOSTYCZNA (Czysta logika, brak zależności od Vue) --
export function validateFile(
  file: File,
  config: FileValidatorConfig,
): FileValidationError | null {
  if (!(file instanceof File)) return 'NOT_A_FILE'
  if (file.size > config.maxSize) return 'TOO_BIG'
  if (!config.allowedTypes.includes(file.type)) return 'UNSUPPORTED_FORMAT'

  return null
}

const ERROR_MESSAGES: Record<FileValidationError, string> = {
  NOT_A_FILE: 'Selected item is not a file',
  TOO_BIG: 'File is too big',
  UNSUPPORTED_FORMAT: 'Unsupported format',
}

// -- WARSTWA VUE (Reaktywność i cykl życia) --
export interface UseFilePreviewOptions {
  maxSize: MaybeRefOrGetter<number>
  allowedTypes: MaybeRefOrGetter<string[]>
}

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
    // Ciche przerwanie, gdy użytkownik anulował wybór pliku (Standard UX)
    if (!file) return

    const errorType = validateFile(file, {
      maxSize: toValue(options.maxSize),
      allowedTypes: toValue(options.allowedTypes),
    })

    reset()

    if (errorType) {
      errorMessage.value = ERROR_MESSAGES[errorType]
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
