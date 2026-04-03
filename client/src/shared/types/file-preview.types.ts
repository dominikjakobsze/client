export type FileValidationError = 'NOT_A_FILE' | 'TOO_BIG' | 'UNSUPPORTED_FORMAT'

export interface FileValidatorConfig {
  maxSize: number
  allowedTypes: string[]
}

export interface UseFilePreviewOptions {
  maxSize: import('vue').MaybeRefOrGetter<number>
  allowedTypes: import('vue').MaybeRefOrGetter<string[]>
}
