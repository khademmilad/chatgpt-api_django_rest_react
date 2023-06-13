import React from 'react';
import { useForm } from 'react-hook-form';

function Form() {
  const { register, handleSubmit } = useForm();

  const onSubmit = async (data) => {
    // Send the form data to your Django backend
    const response = await fetch('/api/save-form', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      console.log('Form submitted successfully!');
      // Perform any desired actions after successful form submission
    } else {
      console.error('Form submission failed.');
      // Handle form submission failure
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>Name</label>
        <input type="text" {...register('name', { required: true })} />
      </div>

      <div>
        <label>Email</label>
        <input type="email" {...register('email', { required: true })} />
      </div>

      <div>
        <label>Message</label>
        <textarea {...register('message', { required: true })} />
      </div>

      <button type="submit">Submit</button>
    </form>
  );
}

export default Form;
