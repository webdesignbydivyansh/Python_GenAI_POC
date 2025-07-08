import axios from 'axios'

export const fetchVideo = async (player: string) => {
  const response = await axios.post(`/api/video`, {player})
  console.log(response.data);
  
  return response.data
}
