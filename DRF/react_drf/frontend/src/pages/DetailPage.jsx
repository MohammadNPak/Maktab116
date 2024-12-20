import React from 'react';
import { useParams } from 'react-router-dom';

const DetailPage = () => {
  const { id } = useParams();

  return (
    <div>
      <h1>Post Detail</h1>
      <p>Displaying details for post with ID: {id}</p>
    </div>
  );
};

export default DetailPage;
