import type { FileValidationError, FileValidatorConfig } from '@/shared/types/file-preview.types'

export const FILE_VALIDATION_MESSAGES: Record<FileValidationError, string> = {
  NOT_A_FILE: 'Selected item is not a file',
  TOO_BIG: 'File is too big',
  UNSUPPORTED_FORMAT: 'Unsupported format',
}

export function validateFile(
  file: File,
  config: FileValidatorConfig,
): FileValidationError | null {
  if (!(file instanceof File)) return 'NOT_A_FILE'
  if (file.size > config.maxSize) return 'TOO_BIG'
  if (!config.allowedTypes.includes(file.type)) return 'UNSUPPORTED_FORMAT'

  return null
}
