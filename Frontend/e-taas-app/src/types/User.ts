export interface User {
  username: string
  email: string
  first_name: string
  last_name: string
  middle_name?: string
  birth_date?: string
  address?: string
  contact_number?: string
  is_active: boolean
  is_admin: boolean
}