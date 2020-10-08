import { CommentComponent } from './alltopics/topic/post/comment/comment.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { AlltopicsComponent } from './alltopics/alltopics.component';
import { ProfileComponent } from './profile/profile.component';

const routes: Routes = [
  { path: '', redirectTo: '/', pathMatch: 'full' },
  { path: 'login', component:LoginComponent},
  { path: 'signup', component:SignupComponent},
  { path: 'alltopics', component:AlltopicsComponent},
  { path: 'comment-test', component:CommentComponent},
  { path: 'profile', component:ProfileComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
